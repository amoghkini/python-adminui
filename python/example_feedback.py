from adminui import *

app = AdminApp()

def on_submit(form_data):
    print(form_data)

def on_change(value, values):
    print(value)
    print(values)

@app.page('/', 'Feedback')
def form_page():
    return [
        Card(content=[
            Empty(content=[
                Button('Reload', style='primary')
            ]),
            Empty('hello empty', simple_style=True),
            Result('The program runs successfully', sub_title='Subtitle is successful too', 
                content=[Paragraph('I have to say it is a success')], extra=[Button('Go Again', style='primary')]
                )
        ])
    ]

if __name__ == '__main__':
    app.run()