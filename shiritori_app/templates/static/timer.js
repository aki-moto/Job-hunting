function startCountdown(seconds) {
  let timeLeft = seconds;
  const timerElem = document.getElementById("timer");
  const countdown = setInterval(() => {
    timeLeft--;
    timerElem.textContent = timeLeft;
    if (timeLeft <= 0) {
      clearInterval(countdown);
      alert("時間切れです！");
      window.location.href = "/timeout";
    }
  }, 1000);
}
