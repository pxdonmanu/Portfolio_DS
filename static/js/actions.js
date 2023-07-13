let menu = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

menu.onclick = () => {
  menu.classList.toggle("bx-x");
  navbar.classList.toggle("open");
};

document.addEventListener('DOMContentLoaded', function() {
  var prjWrapper = document.querySelector('.prj-wrapper');
  var projectItems = prjWrapper.querySelectorAll('.project');
  var slideContainer = document.querySelector('.slide-container');
  var btnNext = slideContainer.querySelector('.btn-next');
  var btnBack = slideContainer.querySelector('.btn-back');
  var slideIndex = 0;
  var projectsPerPage = 3;

  // Mostrar los proyectos iniciales
  showProjects();

  // Agregar evento al botón "Siguiente"
  btnNext.addEventListener('click', function() {
    slideIndex++;
    showProjects();
  });

  // Agregar evento al botón "Atrás"
  btnBack.addEventListener('click', function() {
    slideIndex--;
    showProjects();
  });

  // Agregar evento al cambio de tamaño de ventana
  window.addEventListener('resize', function() {
    checkWindowSize();
  });

  function showProjects() {
    var startIndex = slideIndex * projectsPerPage;
    var endIndex = startIndex + projectsPerPage;

    // Mostrar solo los proyectos correspondientes al índice actual
    projectItems.forEach(function(project, index) {
      if (index >= startIndex && index < endIndex) {
        project.style.display = 'block';
      } else {
        project.style.display = 'none';
      }
    });

    // Mostrar/ocultar los botones de navegación según el índice
    if (slideIndex === 0) {
      btnBack.style.display = 'none';
    } else {
      btnBack.style.display = 'block';
    }

    if (endIndex >= projectItems.length) {
      btnNext.style.display = 'none';
    } else {
      btnNext.style.display = 'block';
    }
  }

  function checkWindowSize() {
    var windowWidth = window.innerWidth;

    if (windowWidth <= 1400) {
      projectsPerPage = 2;
    } else {
      projectsPerPage = 3;
    }

    // Actualizar la visualización de los proyectos según la nueva cantidad por página
    showProjects();
  }
});


// Timeline

const line= document.querySelector('.timeline-innerline');
const timeline_events= document.querySelectorAll('.ul-timeline .li-timeline');

let observer=new IntersectionObserver((entries, observer)=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting){
      line.style.width=`100%`;
    }
  });
}, {});

let target=document.querySelector('.ul-timeline');
observer.observe(target);