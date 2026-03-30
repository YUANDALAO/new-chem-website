---
layout: default
title: Chemical Library
permalink: /chemlib/
---

<style>
  .chem-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 40px 20px;
  }

  .header-section {
    text-align: center;
    margin-bottom: 50px;
  }

  .header-section h1 {
    font-size: 2.8em;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 15px;
  }

  .header-section p {
    color: #666;
    font-size: 1.1em;
  }

  .controls-section {
    display: flex;
    gap: 15px;
    margin-bottom: 40px;
    flex-wrap: wrap;
    justify-content: center;
  }

  .search-box {
    flex: 1;
    min-width: 300px;
    max-width: 500px;
  }

  .search-box input {
    width: 100%;
    padding: 12px 20px;
    border: 2px solid #e0e0e0;
    border-radius: 25px;
    font-size: 1em;
    transition: all 0.3s;
    outline: none;
  }

  .search-box input:focus {
    border-color: #999;
    box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.03);
  }

  .molecule-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 30px;
    padding: 20px 0;
  }

  .molecule-card {
    background: white;
    border: 1px solid #e8e8e8;
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
    transition: all 0.35s;
    display: flex;
    flex-direction: column;
  }

  .molecule-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.08);
    border-color: #bbb;
  }

  .molecule-card .structure {
    width: 100%;
    height: 250px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #ffffff;
    border-radius: 12px;
    margin-bottom: 16px;
    position: relative;
    overflow: visible;
    border: 1px solid #f0f0f0;
    flex-shrink: 0;
  }

  .molecule-card .structure img {
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    display: block;
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }

  .molecule-card .mol-id {
    font-weight: 600;
    color: #1a1a1a;
    font-family: 'Monaco', 'Menlo', monospace;
    font-size: 1.15em;
    margin-top: auto;
    cursor: pointer;
    transition: all 0.3s;
    padding-top: 12px;
    letter-spacing: 0.5px;
  }

  .molecule-card .mol-id:hover {
    color: #2c3e50;
    transform: scale(1.05);
  }

  @media (max-width: 768px) {
    .molecule-grid {
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 20px;
    }
    
    .molecule-card {
      padding: 20px;
    }
    
    .molecule-card .structure {
      height: 210px;
    }
  }
</style>

<div class="chem-container">
  <div class="header-section">
    <h1>Chemical Library</h1>
    <p></p>
  </div>

  <div class="controls-section">
    <div class="search-box">
      <input type="text" id="searchInput" placeholder="🔍 Search by ID...">
    </div>
  </div>

  <div class="molecule-grid" id="moleculeGrid">
    {% for molecule in site.data.molecules %}
      <div class="molecule-card" data-id="{{ molecule.ID }}">
        <div class="structure">
          <img loading="lazy" src="{{ site.baseurl }}/assets/images/compounds/{{ molecule.ID }}.svg" 
               alt="{{ molecule.ID }}"
               loading="lazy">
        </div>
        <p class="mol-id" title="Click to copy">{{ molecule.ID }}</p>
      </div>
    {% endfor %}
  </div>
</div>

<script>
  const searchInput = document.getElementById('searchInput');
  const cards = document.querySelectorAll('.molecule-card');

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    cards.forEach(card => {
      const id = card.dataset.id.toLowerCase();
      card.style.display = id.includes(query) ? '' : 'none';
    });
  });

  document.querySelectorAll('.mol-id').forEach(label => {
    label.addEventListener('click', () => {
      const text = label.textContent;
      navigator.clipboard.writeText(text).then(() => {
        const original = label.textContent;
        label.textContent = '✓ Copied!';
        setTimeout(() => label.textContent = original, 1500);
      });
    });
  });
</script>