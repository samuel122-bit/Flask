let quizData = [{
  question: 'what is the full meaning of html',
  options: ['hyper text markup language', 'human resource locator', 'uniform resource locator', 'hyper text transfer protocol'],
  answer:0
}, {
  question:'which of the following is used as styling web page',
  options:['html', 'css', 'js', 'react'],
  answer:1
}]
quizData.sort(() => Math.random()-0.5)
let timeQuestion = document.getElementById('timer')
let time = 10
let question = document.getElementById('question')
let optionBtn = document.querySelectorAll('.option')
let currentQuestion = 0
let score = 0
let countdown;
function loadQuestion() {
  clearInterval(countdown)
  time = 10
  timeQuestion.textContent = "Time: 10s"
  let q = quizData[currentQuestion]
  question.innerText = q.question
  optionBtn.forEach((button, index) => {
    button.textContent = q.options[index]
    button.className ='option'
    button.onclick = function () {
      if (index === q.answer) {
        button.classList.add('correct')
        score++
      } else {
        button.classList.add('wrong')
      }
      optionBtn.forEach(b => b.disabled = true)
    }
  })
  startTimer()
  updateprogress()
}
let nextBtn = document.getElementById('nextBtn')
nextBtn.onclick = function () {
    currentQuestion++;

    if (currentQuestion < quizData.length) {
      optionBtn.forEach(b => b.disabled = false)
        loadQuestion();
    } else {
        showResult();
    }
};
function showResult() {
  localStorage.setItem('score', score)
    document.querySelector(".quiz-container").innerHTML =
        `<h2>Your Score: ${score}/${quizData.length}<br> your percentage is: ${(score / quizData.length) * 100}% </h2>
        <br>
        <button onclick="location.reload()">reset quiz</button>`;
}
let progressBar = document.getElementById('progress-Bar')
function updateprogress() {
  let progress = ((currentQuestion + 1) / quizData.length ) * 100
  progressBar.style.width = progress + '%'
}
function previousQuestion() {
    currentQuestion--
    if (currentQuestion < quizData.length) {
            optionBtn.forEach(b => b.disabled = false)
        loadQuestion()
    }
}
function startTimer() {
  countdown = setInterval(() => {
    time--
    timeQuestion.textContent = 
    `Time: ${time}s`
    if (time === 0) {
      clearInterval(countdown)
      optionBtn.forEach(b => {
        b.disabled = true
      })
    }
  }, 1000)
}
loadQuestion()
