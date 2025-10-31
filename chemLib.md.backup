---
layout: default
title: Chemical Library
permalink: /chemlib/
---

<!-- 专业黑白风格 + 性能优化 -->
<style>
  /* 主容器 */
  .chem-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 40px 20px;
  }

  /* 页面标题区 */
  .header-section {
    text-align: center;
    margin-bottom: 50px;
    animation: fadeIn 0.8s ease-in;
  }

  .header-section h1 {
    font-size: 2.8em;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 15px;
    letter-spacing: -0.5px;
  }

  .header-section p {
    color: #666;
    font-size: 1.1em;
    max-width: 600px;
    margin: 0 auto;
  }

  /* 搜索和筛选区 */
  .controls-section {
    display: flex;
    gap: 15px;
    margin-bottom: 30px;
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
    border: 2px solid #ddd;
    border-radius: 25px;
    font-size: 1em;
    transition: all 0.3s;
    outline: none;
  }

  .search-box input:focus {
    border-color: #555;
    box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.05);
  }

  .view-toggle {
    display: flex;
    gap: 10px;
  }

  .view-btn {
    padding: 10px 20px;
    border: 2px solid #ddd;
    background: white;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: 500;
    color: #555;
  }

  .view-btn:hover {
    border-color: #555;
    background: #f8f9fa;
  }

  .view-btn.active {
    background: #333;
    color: white;
    border-color: #333;
  }

  /* 分子网格 */
  .molecule-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 30px;
    padding: 20px 0;
  }

  /* 分子卡片 */
  .molecule-card {
    background: white;
    border: 1px solid #e5e5e5;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    opacity: 0;
    animation: fadeInUp 0.5s ease-out forwards;
  }

  .molecule-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    border-color: #ccc;
  }

  /* 结构容器 */
  .molecule-card .structure {
    width: 100%;
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #fafafa;
    border-radius: 8px;
    margin-bottom: 15px;
    position: relative;
    overflow: hidden;
    border: 1px solid #f0f0f0;
  }

  .molecule-card .structure svg {
    max-width: 100%;
    max-height: 100%;
    position: relative;
    z-index: 1;
  }

  /* 超强黑白转换 */
  .molecule-card .structure svg * {
    stroke: #000000 !important;
  }

  .molecule-card .structure svg path,
  .molecule-card .structure svg line,
  .molecule-card .structure svg polyline,
  .molecule-card .structure svg ellipse,
  .molecule-card .structure svg circle {
    stroke: #000000 !important;
  }

  .molecule-card .structure svg text {
    fill: #000000 !important;
    stroke: none !important;
  }

  .molecule-card .structure svg rect[fill="#FFFFFF"],
  .molecule-card .structure svg ellipse[fill="#FFFFFF"] {
    fill: #FFFFFF !important;
  }

  /* 加载动画 */
  .loading {
    display: inline-block;
    width: 30px;
    height: 30px;
    border: 3px solid #e0e0e0;
    border-top-color: #555;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  /* 占位符（懒加载用） */
  .placeholder {
    color: #999;
    font-size: 0.9em;
  }

  /* 分子ID标签 */
  .molecule-card .mol-id {
    font-weight: 600;
    color: #2c3e50;
    font-family: 'Monaco', 'Menlo', monospace;
    font-size: 1.1em;
    margin-top: 10px;
    cursor: pointer;
    transition: color 0.3s;
  }

  .molecule-card .mol-id:hover {
    color: #000;
  }

  /* 错误提示 */
  .error-msg {
    color: #d63031;
    font-size: 0.9em;
    padding: 10px;
    background: #ffe5e5;
    border-radius: 8px;
  }

  /* 动画 */
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  /* 响应式 */
  @media (max-width: 768px) {
    .molecule-grid {
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 20px;
    }
    
    .header-section h1 {
      font-size: 2em;
    }
  }

  ::selection {
    background: #333;
    color: white;
  }
</style>

<!-- 页面内容 -->
<div class="chem-container">
  <div class="header-section">
    <h1>Chemical Library</h1>
    <p>Explore our collection with interactive 2D structures</p>
  </div>

  <div class="controls-section">
    <div class="search-box">
      <input type="text" id="searchInput" placeholder="🔍 Search by ID...">
    </div>
    <div class="view-toggle">
      <button class="view-btn active" data-view="grid">Grid View</button>
      <button class="view-btn" data-view="list">List View</button>
    </div>
  </div>

  <div class="molecule-grid" id="moleculeGrid">
    {% for molecule in site.data.molecules %}
      <div class="molecule-card" data-id="{{ molecule.ID }}" style="animation-delay: {{ forloop.index | times: 0.03 }}s">
        <div class="structure" data-smiles="{{ molecule.SMILES }}">
          <div class="placeholder">Loading...</div>
        </div>
        <p class="mol-id" title="Click to copy">{{ molecule.ID }}</p>
      </div>
    {% endfor %}
  </div>
</div>

<!-- 预加载RDKit -->
<link rel="preload" href="https://unpkg.com/@rdkit/rdkit/Code/MinimalLib/dist/RDKit_minimal.js" as="script">

<!-- RDKit库 -->
<script src="https://unpkg.com/@rdkit/rdkit/Code/MinimalLib/dist/RDKit_minimal.js"></script>

<!-- 主脚本 - 性能优化版本（带懒加载） -->
<script>
  // 配置（性能优化）
  const CONFIG = {
    lazyLoad: true,        // 启用懒加载
    batchSize: 10,         // 减少批量大小
    renderDelay: 150,      // 增加延迟
    lazyMargin: '100px'    // 提前加载边距
  };

  let RDKitInstance = null;

  // 超强黑白转换函数
  function forceBlackAndWhite(svgElement) {
    if (!svgElement) return;
    
    const allElements = svgElement.querySelectorAll('*');
    allElements.forEach(el => {
      const tagName = el.tagName.toLowerCase();
      
      if (tagName === 'text') {
        el.setAttribute('fill', '#000000');
        el.setAttribute('stroke', 'none');
        el.style.fill = '#000000';
        el.style.stroke = 'none';
      } else if (tagName === 'path' || tagName === 'line' || tagName === 'polyline' || tagName === 'ellipse' || tagName === 'circle') {
        const currentFill = el.getAttribute('fill');
        const currentStroke = el.getAttribute('stroke');
        
        if (currentStroke && currentStroke !== 'none') {
          el.setAttribute('stroke', '#000000');
          el.style.stroke = '#000000';
        }
        
        if (currentFill && currentFill !== 'none' && currentFill.toLowerCase() !== '#ffffff' && currentFill.toLowerCase() !== 'white') {
          el.setAttribute('fill', '#000000');
          el.style.fill = '#000000';
        }
      }
    });
  }

  // 绘制单个分子
  function drawMolecule(holder, RDKit) {
    const smiles = holder.dataset.smiles;
    if (!smiles || !smiles.trim()) return;

    try {
      const mol = RDKit.get_mol(smiles);
      if (mol && mol.is_valid()) {
        const svg = mol.get_svg(200, 200);
        holder.innerHTML = svg;
        
        const svgElement = holder.querySelector('svg');
        forceBlackAndWhite(svgElement);
        
        mol.delete();
      } else {
        holder.innerHTML = '<div class="error-msg">Invalid SMILES</div>';
      }
    } catch (e) {
      console.error(`Error rendering: ${smiles}`, e);
      holder.innerHTML = '<div class="error-msg">Render Error</div>';
    }
  }

  // 懒加载功能（性能优化关键）
  function setupLazyLoading(RDKit) {
    const observerOptions = {
      root: null,
      rootMargin: CONFIG.lazyMargin,
      threshold: 0.01
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const holder = entry.target.querySelector('.structure');
          if (holder && holder.dataset.smiles && !holder.dataset.loaded) {
            // 添加加载动画
            holder.innerHTML = '<div class="loading"></div>';
            
            // 延迟渲染以避免阻塞
            setTimeout(() => {
              drawMolecule(holder, RDKit);
              holder.dataset.loaded = 'true';
            }, 50);
          }
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    document.querySelectorAll('.molecule-card').forEach(card => {
      observer.observe(card);
    });
  }

  // 批量渲染（非懒加载模式）
  function renderBatch(molecules, startIndex, RDKit) {
    const endIndex = Math.min(startIndex + CONFIG.batchSize, molecules.length);
    
    for (let i = startIndex; i < endIndex; i++) {
      const holder = molecules[i];
      holder.innerHTML = '<div class="loading"></div>';
      drawMolecule(holder, RDKit);
    }

    if (endIndex < molecules.length) {
      setTimeout(() => {
        renderBatch(molecules, endIndex, RDKit);
      }, CONFIG.renderDelay);
    }
  }

  // 搜索功能
  function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    const cards = document.querySelectorAll('.molecule-card');

    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase();
      cards.forEach(card => {
        const id = card.dataset.id.toLowerCase();
        card.style.display = id.includes(query) ? '' : 'none';
      });
    });
  }

  // 视图切换
  function setupViewToggle() {
    const buttons = document.querySelectorAll('.view-btn');
    const grid = document.getElementById('moleculeGrid');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        const view = btn.dataset.view;
        if (view === 'list') {
          grid.style.gridTemplateColumns = '1fr';
        } else {
          grid.style.gridTemplateColumns = 'repeat(auto-fill, minmax(240px, 1fr))';
        }
      });
    });
  }

  // 复制ID
  function setupCopyId() {
    document.querySelectorAll('.mol-id').forEach(label => {
      label.addEventListener('click', () => {
        const text = label.textContent;
        navigator.clipboard.writeText(text).then(() => {
          const original = label.textContent;
          label.textContent = '✓ Copied!';
          setTimeout(() => {
            label.textContent = original;
          }, 1500);
        });
      });
    });
  }

  // 初始化
  window.initRDKitModule().then((RDKit) => {
    RDKitInstance = RDKit;
    window.RDKit = RDKit;
    console.log('✓ RDKit loaded successfully');

    const initPage = () => {
      const moleculeHolders = document.querySelectorAll('.structure[data-smiles]');
      console.log(`Found ${moleculeHolders.length} molecules`);
      console.log(`Lazy loading: ${CONFIG.lazyLoad ? 'enabled' : 'disabled'}`);
      
      // 根据配置选择渲染方式
      if (CONFIG.lazyLoad) {
        setupLazyLoading(RDKit);
      } else {
        renderBatch(Array.from(moleculeHolders), 0, RDKit);
      }
      
      setupSearch();
      setupViewToggle();
      setupCopyId();
    };

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initPage);
    } else {
      initPage();
    }
  }).catch((e) => {
    console.error('✗ RDKit initialization failed:', e);
    const grid = document.getElementById('moleculeGrid');
    if (grid) {
      grid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 60px;">
          <h2 style="color: #d63031;">Failed to load RDKit</h2>
          <p>Please refresh the page or check your internet connection</p>
        </div>
      `;
    }
  });
</script>