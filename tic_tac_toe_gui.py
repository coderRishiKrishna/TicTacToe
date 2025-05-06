import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QGridLayout, QLabel, QVBoxLayout

class TicTacToe(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Tic Tac Toe Game") 
        self.setGeometry(0, 0, 200, 200) 
        self.xState = [0]*9 
        self.zState = [0]*9 
        self.turn = 1  # 1 for X, 0 for O 
        self.buttons = []
        self.x_wins = 0
        self.o_wins = 0
        self.score_label = QLabel("Score -> X : 0 | O : 0")
        self.score_label.setStyleSheet("font-size: 14px; font-weight: bold; color: orange")

        self.layout = QVBoxLayout()
        self.info_label = QLabel("X's Turn")
        self.info_label.setStyleSheet("font-size: 18px; font-weight: bold; color: green;")
        self.grid_layout = QGridLayout()
        self.initUI()

        self.layout.addWidget(self.info_label)
        self.layout.addWidget(self.score_label)
        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: lightblue;")

    def initUI(self):
        for idx in range(9):
            button = QPushButton(str(idx))
            button.setFixedSize(80, 80)
            button.clicked.connect(lambda _, index=idx: self.button_clicked(index))
            self.grid_layout.addWidget(button, idx // 3, idx % 3)
            self.buttons.append(button)

    def button_clicked(self, index):
        if self.xState[index] or self.zState[index]:
            QMessageBox.warning(self, "Invalid Move", "Position already occupied!")
            return

        if self.turn == 1:
            self.xState[index] = 1
            self.buttons[index].setText("X")
            self.buttons[index].setStyleSheet("background-color: orange; color: white;")
            self.info_label.setText("O's Turn")
        else:
            self.zState[index] = 1
            self.buttons[index].setText("O")
            self.buttons[index].setStyleSheet("background-color: green; color: white;")
            self.info_label.setText("X's Turn")

        result = self.check_win()
        if result != -1:
            if result == 1:
                self.x_wins += 1
                QMessageBox.information(self, "Game Over", "X Won the match!")
            elif result == 0:
                self.o_wins += 1
                QMessageBox.information(self, "Game Over", "O Won the match!")
            self.score_label.setText(f"Score -> X : {self.x_wins} | O : {self.o_wins}")
            self.ask_replay()
            return
        elif sum(self.xState) + sum(self.zState) == 9:
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.ask_replay()
            return

        self.turn = 1 - self.turn

    def check_win(self):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
        for win in wins:
            if self.xState[win[0]] + self.xState[win[1]] + self.xState[win[2]] == 3:
                return 1
            if self.zState[win[0]] + self.zState[win[1]] + self.zState[win[2]] == 3:
                return 0
        return -1

    def ask_replay(self):
        reply = QMessageBox.question(self, "Play Again", "Do you want to play again?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reset_game()
        else:
            QApplication.quit()

    def reset_game(self):
        self.xState = [0]*9
        self.zState = [0]*9
        self.turn = 1
        self.info_label.setText("X's Turn")
        for idx in range(9):
            self.buttons[idx].setText(str(idx))
            self.buttons[idx].setStyleSheet("")
        

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    window = TicTacToe() 
    window.show() 
    sys.exit(app.exec_())
