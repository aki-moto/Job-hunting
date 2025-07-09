from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "shiritori_secret"

def get_next_turn(current_turn, alive):
    n = len(alive)
    for i in range(1, n + 1):
        next_turn = (current_turn + i) % n
        if alive[next_turn]:
            return next_turn
    return -1  # 全員脱落

@app.route("/", methods=["GET", "POST"])
def setup():
    if request.method == "POST":
        players = int(request.form["players"])
        session.update({
            "players": players,
            "turn": 0,
            "counts": [0] * players,
            "alive": [True] * players,
            "history": [],
            "freedom": False,
            "eliminated": [],
            "violations": [0] * players,
        })
        return redirect(url_for("play"))
    return render_template("setup.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    if "players" not in session:
        return redirect(url_for("setup"))

    players = session.get("players")
    history = session.get("history", [])
    counts = session.get("counts", [])
    turn = session.get("turn", 0)
    alive = session.get("alive", [])
    eliminated = session.get("eliminated", [])
    freedom = session.get("freedom", False)
    violations = session.get("violations", [0] * players)

    # aliveの型チェック＆変換（念のため）
    alive = [bool(a) for a in alive]

    message = ""
    show_timer = counts[turn] >= 4

    if request.method == "POST":
        word = request.form["word"].strip()

        if not word:
            message = "単語を入力してください。"
            return render_template("index.html", players=players, turn=turn, counts=counts, alive=alive,
                                   history=history, message=message, show_timer=show_timer, freedom=freedom,
                                   violations=violations)

        if not freedom and history:
            last_char = history[-1][-1]
            if word[0] != last_char:
                violations[turn] += 1
                if violations[turn] >= 2:
                    alive[turn] = False
                    eliminated.append(turn)
                    message = f"プレイヤー{turn + 1}が2回間違えたため脱落しました！"
                    turn = get_next_turn(turn, alive)
                    session.update({
                        "alive": alive,
                        "eliminated": eliminated,
                        "turn": turn,
                        "violations": violations
                    })
                    # 脱落後勝利判定
                    if sum(alive) == 1:
                        return redirect(url_for("win"))
                    return redirect(url_for("play"))
                else:
                    message = f"前の単語の最後の文字 '{last_char}' から始まっていません（警告: {violations[turn]}回目）。"
                    session["violations"] = violations
                    return render_template("index.html", players=players, turn=turn, counts=counts, alive=alive,
                                           history=history, message=message, show_timer=show_timer, freedom=freedom,
                                           violations=violations)

        if word in history:
            message = "すでに使われた単語です。"
            return render_template("index.html", players=players, turn=turn, counts=counts, alive=alive,
                                   history=history, message=message, show_timer=show_timer, freedom=freedom,
                                   violations=violations)

        if word[-1] == "ん":
            alive[turn] = False
            eliminated.append(turn)
            message = f"プレイヤー{turn + 1}が「ん」で脱落しました！"
            session["freedom"] = True
            turn = get_next_turn(turn, alive)
            session.update({
                "alive": alive,
                "eliminated": eliminated,
                "turn": turn,
                "violations": violations,
            })
            if sum(alive) == 1:
                return redirect(url_for("win"))
            return redirect(url_for("play"))
        else:
            history.append(word)
            counts[turn] += 1
            session["freedom"] = False

        if sum(alive) == 1:
            session.update({
                "history": history,
                "counts": counts,
                "alive": alive,
                "eliminated": eliminated,
                "violations": violations
            })
            return redirect(url_for("win"))

        session.update({
            "history": history,
            "counts": counts,
            "alive": alive,
            "eliminated": eliminated,
            "turn": get_next_turn(turn, alive),
            "violations": violations
        })

        return redirect(url_for("play"))

    return render_template("index.html", players=players, turn=turn, counts=counts, alive=alive,
                           history=history, message=message, show_timer=show_timer, freedom=freedom,
                           violations=violations)

@app.route("/timeout")
def timeout():
    turn = session.get("turn", 0)
    alive = session.get("alive", [])
    eliminated = session.get("eliminated", [])

    alive = [bool(a) for a in alive]  # 念のため型変換

    alive[turn] = False
    eliminated.append(turn)
    session["freedom"] = True

    if sum(alive) == 1:
        session.update({"alive": alive, "eliminated": eliminated})
        return redirect(url_for("win"))

    session.update({
        "alive": alive,
        "eliminated": eliminated,
        "turn": get_next_turn(turn, alive),
    })
    return redirect(url_for("play"))

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("setup"))

@app.route("/win")
def win():
    alive = session.get("alive", [])
    alive = [bool(a) for a in alive]  # 念のため型変換
    winner = None
    for i, a in enumerate(alive):
        if a:
            winner = i + 1
            break
    return render_template("win.html", winner=winner)

if __name__ == "__main__":
    app.run(debug=True)
