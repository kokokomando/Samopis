from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

wagi = [1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7]

slownik_znakow = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    'X': 10, 'A': 11, 'B': 12, 'C': 13, 'D': 14,
    'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24,
    'O': 25, 'P': 26, 'R': 27, 'S': 28, 'T': 29,
    'U': 30, 'W': 31, 'Y': 32, 'Z': 33
}


@app.route('/', methods=['POST', 'GET'])
def calculate_kontrolna():
    if request.method == 'POST':
        data = request.form
        input1 = data['input1']
        input2 = data['input2']
        kwtest = input1 + input2

        KW2 = kwtest.replace("/", "")

        char_list = [char for char in KW2]

        replaced_list = [slownik_znakow[char] if char in slownik_znakow else char for char in char_list]

        numbers = replaced_list

        multiplied_list = [num * weight for num, weight in zip(numbers, wagi)]

        total = sum(multiplied_list)

        kontrolna = total % 10

        return jsonify({'kontrolna': kontrolna})

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
