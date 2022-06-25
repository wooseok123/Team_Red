const imgs = document.getElementsByTagName("img");

const handleImg = (event) => {
  console.log(event.path[1]);
};

Array.from(imgs).forEach((img) => {
  img.addEventListener("mouseover", handleImg);
});

setTimeout(() => {
  projects.forEach((project) => {
    if (filter == "*" || filter == project.dataset.type) {
      project.classList.remove("invisible");
    } else {
      project.classList.add("invisible");
    }
    projectContainer.classList.remove("anim-out");
  });
}, 300);
