function addReviewsSpoiler() {
    document.querySelectorAll(".reviews__card").forEach(e => {
        let t = e.querySelector(".reviews__card-text");
        let windowWidth = window.innerWidth;

        if (windowWidth > 990) {
            if (t.scrollHeight > 280) {
                let l = document.createElement("button");
                l.classList.add("review-card__toggle", "active"), l.innerText = "Читать полностью", l.addEventListener("click", function() {
                    t.classList.contains("expanded") ? (t.classList.remove("expanded"), l.innerText = "Читать полностью") : (t.classList.add("expanded"), l.innerText = "Свернуть")
                }), t.after(l)
            }
        }
        else {
            if (t.scrollHeight > 200) {
                let l = document.createElement("button");
                l.classList.add("review-card__toggle", "active"), l.innerText = "Читать полностью", l.addEventListener("click", function() {
                    t.classList.contains("expanded") ? (t.classList.remove("expanded"), l.innerText = "Читать полностью") : (t.classList.add("expanded"), l.innerText = "Свернуть")
                }), t.after(l)
            }
        }
    })
}
document.addEventListener("DOMContentLoaded", () => {
    addReviewsSpoiler();
});