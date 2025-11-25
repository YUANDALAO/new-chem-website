---
layout: default
title: Research
permalink: /assay/
---

<style>
  .research-section { margin-bottom: 4rem; }
  .section-header { 
    text-align: center; 
    margin: 2rem 0 3rem; 
    padding-bottom: 1rem;
    border-bottom: 2px solid #f0f0f0;
  }
  .section-header h2 { 
    color: #2c3e50; 
    margin: 0;
    font-size: 1.8rem;
  }
  .research-grid { 
    display: grid; 
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); 
    gap: 1.8rem; 
    padding: 0 1rem;
  }
  .research-card { 
    border: 1px solid #e0e0e0; 
    padding: 1.8rem; 
    border-radius: 10px; 
    text-decoration: none; 
    color: inherit; 
    display: flex; 
    flex-direction: column; 
    transition: all 0.3s ease; 
    background: #fff;
    height: 100%;
    box-sizing: border-box;
  }
  .research-card:hover { 
    transform: translateY(-6px); 
    box-shadow: 0 12px 20px rgba(0,0,0,0.08); 
    border-color: #3498db; 
  }
  .research-card h3 { 
    margin-top: 0; 
    color: #2c3e50; 
    border-bottom: 2px solid #f5f5f5; 
    padding-bottom: 0.8rem; 
    margin-bottom: 1.2rem; 
    font-size: 1.3rem;
  }
  .research-card p { 
    font-size: 1em; 
    line-height: 1.7; 
    margin-bottom: 1.5rem; 
    flex-grow: 1; 
    color: #555;
  }
  .read-more-link { 
    font-weight: 600; 
    align-self: flex-end; 
    color: #3498db;
    transition: color 0.2s ease;
    display: inline-flex;
    align-items: center;
  }
  .read-more-link:hover {
    color: #2980b9;
  }
  .read-more-link::after {
    content: "→";
    margin-left: 0.5rem;
    transition: transform 0.2s ease;
  }
  .research-card:hover .read-more-link::after {
    transform: translateX(3px);
  }
</style>

<h1 style="text-align: center; margin: 2rem 0 1rem; color: #2c3e50;">Assay Development & Applications</h1>
<hr style="max-width: 80px; margin: 0 auto 2rem; border: 1px solid #3498db;">

<!-- Chemical Assay Section -->
<div class="research-section">
  <div class="section-header">
    <h2>Chemical Assays</h2>
  </div>
  <div class="research-grid">
    <a href="{{ '/research/chemical-assays/enzymatic/' | relative_url }}" class="research-card">
      <h3>Enzymatic Activity Assays</h3>
      <p>Development of high-throughput chemical assays to measure enzyme kinetics, inhibition constants, and substrate specificity for drug target validation.</p>
      <span class="read-more-link">Learn More</span>
    </a>

    <a href="{{ '/research/chemical-assays/binding/' | relative_url }}" class="research-card">
      <h3>Molecular Binding Assays</h3>
      <p>Design of fluorescence-based and SPR-based chemical assays to quantify biomolecular interactions between small molecules and target proteins.</p>
      <span class="read-more-link">Explore Methods</span>
    </a>

    <a href="{{ '/research/chemical-assays/metabolite/' | relative_url }}" class="research-card">
      <h3>Metabolite Detection Assays</h3>
      <p>Development of LC-MS/MS based chemical assays for sensitive quantification of endogenous metabolites in biological samples.</p>
      <span class="read-more-link">View Protocols</span>
    </a>
  </div>
</div>

<!-- Cell Assay Section -->
<div class="research-section">
  <div class="section-header">
    <h2>Cellular Assays</h2>
  </div>
  <div class="research-grid">
    <a href="{{ '/research/cell-assays/cytotoxicity/' | relative_url }}" class="research-card">
      <h3>Cytotoxicity & Viability Assays</h3>
      <p>Optimization of cell-based assays to evaluate compound toxicity, including MTT, LDH release, and live/dead staining protocols.</p>
      <span class="read-more-link">Learn More</span>
    </a>

    <a href="{{ '/research/cell-assays/signaling/' | relative_url }}" class="research-card">
      <h3>Cell Signaling Assays</h3>
      <p>Development of reporter gene and phosphorylation-based cell assays to study pathway modulation by small molecule compounds.</p>
      <span class="read-more-link">Explore Pathways</span>
    </a>

    <a href="{{ '/research/cell-assays/imaging/' | relative_url }}" class="research-card">
      <h3>High-Content Imaging Assays</h3>
      <p>Integration of automated microscopy and image analysis for cell-based phenotypic screening and subcellular localization studies.</p>
      <span class="read-more-link">View Imaging Data</span>
    </a>
  </div>
</div>