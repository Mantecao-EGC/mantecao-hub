document.addEventListener('DOMContentLoaded', () => {
    send_query();
});

let tagsPopulated = false;

function populateTagsSelect(data) {
    if (tagsPopulated) return;

    const tagsSelect = document.getElementById('tags_select');
    const allTags = new Set();
    data.forEach(dataset => dataset.tags.forEach(tag => allTags.add(tag)));

    tagsSelect.innerHTML = '';
    Array.from(allTags).forEach(tag => {
        const option = new Option(tag, tag);
        tagsSelect.appendChild(option);
    });

    tagsPopulated = true;
}

function send_query() {

    console.log("send query...")

    document.getElementById('results').innerHTML = '';
    document.getElementById("results_not_found").style.display = "none";
    console.log("hide not found icon");

    const filters = document.querySelectorAll('#filters input, #filters select, #filters [type="radio"]');

    filters.forEach(filter => {
        filter.addEventListener('input', () => {
            const csrfToken = document.getElementById('csrf_token').value;

            const searchCriteria = {
                csrf_token: csrfToken,
                query: document.querySelector('#query').value,
                publication_type: document.querySelector('#publication_type').value,
                sorting: document.querySelector('[name="sorting"]:checked').value,
                config_number: document.querySelector('#config_number').value,
                core_features: document.querySelector('#core_features').value
            };

            console.log(document.querySelector('#publication_type').value);

            fetch('/explore', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(searchCriteria),
            })
                .then(response => response.json())
                .then(data => {

                    console.log(data);
                    document.getElementById('results').innerHTML = '';

                    populateTagsSelect(data);
                    
                    // size limit
                    const sizeLimit = parseInt(document.querySelector('#size_limit').value) * 1024 * 1024;
                    let filteredData = data.filter(dataset => dataset.total_size_in_bytes <= sizeLimit);

                    // model count filtering
                    const modelCount = parseInt(document.querySelector('#model_count').value);
                    filteredData = filteredData.filter(dataset => dataset.files_count >= modelCount);

                    // tags filtering
                    const tagsSelect = document.getElementById('tags_select');
                    const selectedTagsList = Array.from(tagsSelect.selectedOptions).map(opt => opt.value);
                    if (selectedTagsList.length > 0) {
                        filteredData = filteredData.filter(dataset =>
                            selectedTagsList.every(tag => dataset.tags.includes(tag))
                        );
                    }

                    // size-based sorting
                    const sortingValue = document.querySelector('[name="sorting"]:checked').value;
                    switch (sortingValue) {
                        case "smaller":
                            filteredData.sort((a, b) => a.total_size_in_bytes - b.total_size_in_bytes);
                            break;
                        case "bigger":
                            filteredData.sort((a, b) => b.total_size_in_bytes - a.total_size_in_bytes);
                            break;
                        default:
                            break;
                    }

                    // results counter
                    const resultCount = filteredData.length;
                    const resultText = resultCount === 1 ? 'dataset' : 'datasets';
                    document.getElementById('results_number').textContent = `${resultCount} ${resultText} found`;

                    if (resultCount === 0) {
                        console.log("show not found icon");
                        document.getElementById("results_not_found").style.display = "block";
                    } else {
                        document.getElementById("results_not_found").style.display = "none";
                    }


                    filteredData.forEach(dataset => {
                        let card = document.createElement('div');
                        card.className = 'col-12';
                        card.innerHTML = `
                            <div class="card">
                                <div class="card-body">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h3><a href="${dataset.url}">${dataset.title}</a></h3>
                                        <div>
                                            <span class="badge bg-primary" style="cursor: pointer;" onclick="set_publication_type_as_query('${dataset.publication_type}')">${dataset.publication_type}</span>
                                        </div>
                                    </div>
                                    <p class="text-secondary">${formatDate(dataset.created_at)}</p>

                                    <div class="row mb-2">

                                        <div class="col-md-4 col-12">
                                            <span class=" text-secondary">
                                                Description
                                            </span>
                                        </div>
                                        <div class="col-md-8 col-12">
                                            <p class="card-text">${dataset.description}</p>
                                        </div>

                                    </div>

                                    <div class="row mb-2">

                                        <div class="col-md-4 col-12">
                                            <span class=" text-secondary">
                                                Authors
                                            </span>
                                        </div>
                                        <div class="col-md-8 col-12">
                                            ${dataset.authors.map(author => `
                                                <p class="p-0 m-0">${author.name}${author.affiliation ? ` (${author.affiliation})` : ''}${author.orcid ? ` (${author.orcid})` : ''}</p>
                                            `).join('')}
                                        </div>

                                    </div>

                                    <div class="row mb-2">

                                        <div class="col-md-4 col-12">
                                            <span class=" text-secondary">
                                                Tags
                                            </span>
                                        </div>
                                        <div class="col-md-8 col-12">
                                            ${dataset.tags.map(tag => `<span class="badge bg-primary me-1" style="cursor: pointer;" onclick="set_tag_as_query('${tag}')">${tag}</span>`).join('')}
                                        </div>

                                    </div>

                                    <div class="row">

                                        <div class="col-md-4 col-12">

                                        </div>
                                        <div class="col-md-8 col-12">
                                            <a href="${dataset.url}" class="btn btn-outline-primary btn-sm" id="search" style="border-radius: 5px;">
                                                View dataset
                                            </a>
                                            <a href="/dataset/download/${dataset.id}" class="btn btn-outline-primary btn-sm" id="search" style="border-radius: 5px;">
                                                Download (${dataset.total_size_in_human_format})
                                            </a>
                                        </div>


                                    </div>

                                </div>
                            </div>
                        `;

                        document.getElementById('results').appendChild(card);
                    });
                });
        });
    });
}

function formatDate(dateString) {
    const options = { day: 'numeric', month: 'long', year: 'numeric', hour: 'numeric', minute: 'numeric' };
    const date = new Date(dateString);
    return date.toLocaleString('en-US', options);
}

function set_tag_as_query(tagName) {
    const queryInput = document.getElementById('query');
    queryInput.value = tagName.trim();
    queryInput.dispatchEvent(new Event('input', { bubbles: true }));
}

function set_publication_type_as_query(publicationType) {
    const publicationTypeSelect = document.getElementById('publication_type');
    for (let i = 0; i < publicationTypeSelect.options.length; i++) {
        if (publicationTypeSelect.options[i].text === publicationType.trim()) {
            // Set the value of the select to the value of the matching option
            publicationTypeSelect.value = publicationTypeSelect.options[i].value;
            break;
        }
    }
    publicationTypeSelect.dispatchEvent(new Event('input', { bubbles: true }));
}

document.getElementById('clear-filters').addEventListener('click', clearFilters);

function clearFilters() {

    // Reset the search query
    let queryInput = document.querySelector('#query');
    queryInput.value = "";
    // queryInput.dispatchEvent(new Event('input', {bubbles: true}));

    // Reset the publication type to its default value
    let publicationTypeSelect = document.querySelector('#publication_type');
    publicationTypeSelect.value = "any"; // replace "any" with whatever your default value is
    // publicationTypeSelect.dispatchEvent(new Event('input', {bubbles: true}));

    // Reset the sorting option
    let sortingOptions = document.querySelectorAll('[name="sorting"]');
    sortingOptions.forEach(option => {
        option.checked = option.value == "newest"; // replace "default" with whatever your default value is
        // option.dispatchEvent(new Event('input', {bubbles: true}));
    });

    // Reset the size limit
    document.getElementById('size_limit').value = 10000;
    document.getElementById('size_limit_value').textContent = '10.000';

    // Reset the model count
    document.getElementById('model_count').value = 0;

    // Reset tags select
    let tagsSelect = document.querySelector('#tags_select');
    Array.from(tagsSelect.options).forEach(option => option.selected = false);

    // Perform a new search with the reset filters
    queryInput.dispatchEvent(new Event('input', { bubbles: true }));
}

document.addEventListener('DOMContentLoaded', () => {

    //let queryInput = document.querySelector('#query');
    //queryInput.dispatchEvent(new Event('input', {bubbles: true}));

    let urlParams = new URLSearchParams(window.location.search);
    let queryParam = urlParams.get('query');

    if (queryParam && queryParam.trim() !== '') {

        const queryInput = document.getElementById('query');
        queryInput.value = queryParam
        queryInput.dispatchEvent(new Event('input', { bubbles: true }));
        console.log("throw event");

    } else {
        const queryInput = document.getElementById('query');
        queryInput.dispatchEvent(new Event('input', { bubbles: true }));
    }
});

// Update size limit display
document.getElementById('size_limit').addEventListener('input', function () {
    document.getElementById('size_limit_value').textContent =
        Number(this.value).toLocaleString();
});