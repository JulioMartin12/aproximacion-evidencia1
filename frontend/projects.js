
function goToProject(projectId) {
    let projectUrl;
  

    switch (projectId) {
      case 1:
        projectUrl = "https://wokwi.com/projects/408580463353840641"; 
        break;
      case 2:
        projectUrl = "https://wokwi.com/projects/408568500712542209"; 
        break;
      case 3:
        projectUrl = "https://wokwi.com/projects/410770508355775489"; 
        break;
      default:
        console.error("Proyecto no encontrado");
        return;
    }
  

    window.open(projectUrl, "_blank");
  }
  