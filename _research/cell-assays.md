---
layout: default
title: Research - Cellular Assays
permalink: /research/cell-assays/
---
<div class="container cell-assays-container">
  <style>
    .cell-assays-container {
      padding: 3rem 0;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    @media (max-width: 768px) {
      .cell-assays-container {
        padding: 5rem 1rem 3rem;
      }
    }
    
    .section-title {
      position: relative;
      display: inline-block;
      margin-bottom: 2.5rem;
      font-weight: 700;
      font-size: 2.5rem;
      color: #2c3e50;
    }
    
    .section-title::after {
      content: '';
      position: absolute;
      left: 0;
      bottom: -8px;
      width: 60px;
      height: 4px;
      background: #3498db;
      border-radius: 2px;
      transition: width 0.5s ease;
    }
    
    .section-title:hover::after {
      width: 100%;
    }
    
    .intro-text {
      font-size: 1.15em;
      line-height: 1.8;
      color: #34495e;
      max-width: 800px;
      margin-bottom: 3rem;
      opacity: 0;
      transform: translateY(20px);
      animation: fadeUp 0.8s ease forwards 0.3s;
    }
    
    .research-section {
      margin-top: 4rem;
    }
    
    .section-header h2 {
      font-size: 1.8rem;
      color: #2c3e50;
      margin-bottom: 2.5rem;
      position: relative;
      padding-bottom: 1rem;
    }
    
    .section-header h2::after {
      content: '';
      position: absolute;
      left: 0;
      bottom: 0;
      width: 40px;
      height: 3px;
      background: #2ecc71;
    }
    
    .research-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 2.5rem;
      perspective: 1000px;
    }
    
    .research-card {
      display: flex;
      flex-direction: column;
      background: #fff;
      border-radius: 12px;
      padding: 2.5rem 1.8rem;
      text-decoration: none;
      color: #34495e;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      border: 1px solid rgba(52, 152, 219, 0.1);
      transform-style: preserve-3d;
      position: relative;
      overflow: hidden;
      opacity: 0;
      transform: translateY(30px) rotateX(-5deg);
    }
    
    .research-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 5px;
      background: linear-gradient(90deg, #3498db, #2ecc71);
      transform: scaleX(0);
      transition: transform 0.4s ease;
    }
    
    .research-card:hover::before {
      transform: scaleX(1);
    }
    
    .research-card h3 {
      color: #2c3e50;
      margin-bottom: 1rem;
      font-size: 1.4rem;
      transition: color 0.3s ease;
      transform: translateZ(20px);
    }
    
    .research-card p {
      flex-grow: 1;
      margin-bottom: 1.8rem;
      line-height: 1.7;
      color: #7f8c8d;
      transition: color 0.3s ease;
      transform: translateZ(15px);
    }
    
    .read-more-link {
      display: inline-flex;
      align-items: center;
      color: #3498db;
      font-weight: 600;
      font-size: 0.95rem;
      transition: all 0.3s ease;
      transform: translateZ(10px);
    }
    
    .read-more-link::after {
      content: '→';
      margin-left: 8px;
      transition: transform 0.3s ease;
    }
    
    .research-card:hover {
      transform: translateY(-10px) rotateX(0) scale(1.02);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
    }
    
    .research-card:hover h3 {
      color: #3498db;
    }
    
    .research-card:hover p {
      color: #555;
    }
    
    .research-card:hover .read-more-link {
      color: #2980b9;
    }
    
    .research-card:hover .read-more-link::after {
      transform: translateX(5px);
    }
    
    /* Animation delays for staggered effect */
    .research-card:nth-child(1) { animation: fadeUp 0.6s ease forwards 0.5s; }
    .research-card:nth-child(2) { animation: fadeUp 0.6s ease forwards 0.7s; }
    .research-card:nth-child(3) { animation: fadeUp 0.6s ease forwards 0.9s; }
    
    @keyframes fadeUp {
      to {
        opacity: 1;
        transform: translateY(0) rotateX(0);
      }
    }
  </style>
  
  <h1 class="section-title">Cellular Assays</h1>
  <p class="intro-text">
    Our cellular assay platforms enable comprehensive evaluation of compound effects on biological systems, providing critical insights into efficacy, toxicity, and mechanism of action. These assays serve as essential tools in our drug discovery pipeline for flavivirus inhibitors and other therapeutic targets.
  </p>

  <!-- Cell Assay Section -->
  <div class="research-section">
    <div class="section-header">
      <h2>Assay Types</h2>
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
</div>