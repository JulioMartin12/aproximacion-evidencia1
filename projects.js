
function goToProject(projectId) {
    let projectUrl;
  

    switch (projectId) {
      case 1:
        projectUrl = "https://wokwi.com/projects/410869104388279297"; 
        break;
      case 2:
        projectUrl = "https://wokwi.com/projects/408568500712542209"; 
        break;
      case 3:
        projectUrl = "https://wokwi.com/projects/410878492815642625"; 
        break;
      case 4:
        projectUrl = "https://wokwi.com/projects/410874071167261697"; 
        break;
      default:
        console.error("Proyecto no encontrado");
        return;
    }
  

    window.open(projectUrl, "_blank");
  }
  