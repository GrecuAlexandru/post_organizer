const fs = require('fs');
const path = require('path');

// Function to create a new section for a specific date
function createSection(date) {
    const section = {
        date,
        photos: [],
        text: ''
    };
    return section;
}

// Function to add a photo to a section
function addPhoto(section, photoPath) {
    section.photos.push(photoPath);
}

// Function to set the text of a section
function setText(section, text) {
    section.text = text;
}

// Function to save the sections into a folder and the text into a JSON file
function saveSections(sections, folderPath, jsonFilePath) {
    // Create the folder if it doesn't exist
    if (!fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath, { recursive: true });
    }

    // Save each section's photos into the folder
    sections.forEach((section, index) => {
        section.photos.forEach((photoPath, photoIndex) => {
            const photoName = `photo_${index}_${photoIndex}${path.extname(photoPath)}`;
            const destinationPath = path.join(folderPath, photoName);
            fs.copyFileSync(photoPath, destinationPath);
        });
    });

    // Save the sections' text into a JSON file
    const jsonContent = JSON.stringify(sections, null, 2);
    fs.writeFileSync(jsonFilePath, jsonContent);
}
