bhai_ye_hai task_game = [
    'bolo "--- Maliklang Rock Paper Scissors ---"',
    'bolo "Game shuru karte hain!"',
    'n1 pucho "Aapka choice (rock/paper/scissors): "',
    'banao comp = __import__(\'random\').choice([\'rock\',\'paper\',\'scissors\'])',
    'bolo "Computer ne chuna: "',
    'bolo comp',
    'agar n1 == comp',
    'bolo "Match Tie ho gaya!"',
    'agar n1 == "paper"',
    'bolo "Aap Jeet Gaye!"',
    'agar n1 == "rock"',
    'bolo "Computer Jeet Gaya!"'
]

chalao_program(task_game)
