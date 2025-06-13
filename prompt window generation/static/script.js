document.getElementById("designForm").addEventListener("submit", async function (e) {
  e.preventDefault(); // Prevent full page reload

  const designText = document.getElementById("designText").value;

  const formData = new FormData();
  formData.append("design", designText);

  try {
    const response = await fetch("/generate", {
      method: "POST",
      body: formData
    });

    const result = await response.json();

    if (response.ok && result.image) {
      const imageUrl = "data:image/png;base64," + result.image;

      // Show image and download
      document.getElementById("previewImage").src = imageUrl;
      document.getElementById("downloadLink").href = imageUrl;
      document.getElementById("designURL").textContent = "Generated using your description";
      document.getElementById("previewSection").style.display = "block";
    } else {
      throw new Error(result.error || "Image generation failed");
    }
  } catch (error) {
    alert("❌ Failed to generate design. Please try again.");
    console.error(error);
  }
});
