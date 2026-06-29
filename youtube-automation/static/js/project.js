document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("imageInput");
    const preview = document.getElementById("previewGrid");
    const counter = document.getElementById("selectedCount");
    const required = document.getElementById("requiredCount");
    const upload = document.getElementById("uploadButton");

    if (!input) return;

    input.addEventListener("change", () => {

        preview.innerHTML = "";

        const total = input.files.length;
        const needed = parseInt(required.innerText);

        counter.innerHTML = total + " / " + needed + " selected";

        upload.disabled = (total !== needed);

        for (const file of input.files) {

            const reader = new FileReader();

            reader.onload = function(e){

                preview.innerHTML += `
                <div class="col-md-3">

                    <div class="card shadow-sm">

                        <img
                            src="${e.target.result}"
                            class="card-img-top"
                            style="height:180px;object-fit:cover;">

                        <div class="card-body">

                            <small>${file.name}</small>

                        </div>

                    </div>

                </div>
                `;

            };

            reader.readAsDataURL(file);

        }

    });

});
