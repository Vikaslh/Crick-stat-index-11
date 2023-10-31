import gradio as gr
import run

team_name = ""
def greet(team, batsman_no, bowler_no, keeper_no):
    team_name = team
    temp = run.select_player(batsman_no, bowler_no, keeper_no)
    out = ""
    for i in temp:
        out = out+i+"\n"
    return out


demo = gr.Interface(
    fn=greet,
    inputs=[
        gr.Dropdown(['India', 'China'], label='Country'),
        gr.Slider(1, 7, step=1),
        gr.Slider(1, 7, step=1),
        gr.Slider(1, 7, step=1)
    ],
    outputs="text"
)

demo.launch()