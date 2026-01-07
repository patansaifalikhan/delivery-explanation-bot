{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fbaf19bd-c668-42f4-a4cb-f861cc2b631f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import base64\n",
    "import os\n",
    "from google import genai\n",
    "from google.genai import types\n",
    "\n",
    "\n",
    "def generate():\n",
    "    client = genai.Client(\n",
    "        api_key=os.environ.get(\"AIzaSyAnLUSLdENDq0nBzNEwiCxlkVgsFNCr6js\"),\n",
    "    )\n",
    "\n",
    "    model = \"gemini-3-flash-preview\"\n",
    "    contents = [\n",
    "        types.Content(\n",
    "            role=\"user\",\n",
    "            parts=[\n",
    "                types.Part.from_text(text=\"\"\"How does grocery order delivery work?\"\"\"),\n",
    "            ],\n",
    "        ),\n",
    "    ]\n",
    "    tools = [\n",
    "        types.Tool(googleSearch=types.GoogleSearch(\n",
    "        )),\n",
    "    ]\n",
    "    generate_content_config = types.GenerateContentConfig(\n",
    "        temperature=0.3,\n",
    "        thinking_config=types.ThinkingConfig(\n",
    "            thinking_level=\"MEDIUM\",\n",
    "        ),\n",
    "        tools=tools,\n",
    "    )\n",
    "\n",
    "    for chunk in client.models.generate_content_stream(\n",
    "        model=model,\n",
    "        contents=contents,\n",
    "        config=generate_content_config,\n",
    "    ):\n",
    "        print(chunk.text, end=\"\")\n",
    "    \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "78303ba3-e11f-4a6e-9789-3627e33ffcdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "     generate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "1dce97b9-683f-453e-a2bd-a5792107c41c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "client = genai.Client(api_key=\"AIzaSyAnLUSLdENDq0nBzNEwiCxlkVgsFNCr6js\")\n",
    "st.title(\"assisstant bot\")\n",
    "query= st.text_input(\"Ask a question\")\n",
    "\n",
    "if st.button(\"Ask\"):\n",
    "    contents= [\n",
    "        types.Content(\n",
    "            role=\"user\",\n",
    "            parts=[types.Part.from_text(text=query)]\n",
    "        )\n",
    "    ]\n",
    "    response = client.models.generate_content(\n",
    "        model = \"gemini-3-flash-preview\",\n",
    "        contents = contents\n",
    "         )\n",
    "    st.write(response.text)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
