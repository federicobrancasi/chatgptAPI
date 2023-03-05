import json
import openai

# import of api key
with open("apikey.json") as f:
    jsonFile = json.load(f)
    api_key = jsonFile["api_key"]

# set api key
openai.api_key = api_key


# function to get response from gpt-3
def get_response(messages_list: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_list,
        temperature=1.0  # from 0.0 to 2.0
    )
    return response.choices[0].message


# main
if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "Sei un assistente virtuale chiamato K e la tua lingua è l'italiano."},
    ]
    try:
        while True:
            user_input = input("\nTu: ")
            messages.append({"role": "user", "content": user_input})
            new_message = get_response(messages)
            print(f"\nK: {new_message['content']}")
            messages.append(new_message)
    except KeyboardInterrupt:
        print("\n\nArrivederci!")
