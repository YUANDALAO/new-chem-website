---
layout: default
title: Chemical Library
permalink: /chemlib/
---

<!-- 现代化样式 -->
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
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 15px;
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
    border: 2px solid #e0e0e0;
    border-radius: 25px;
    font-size: 1em;
    transition: all 0.3s;
    outline: none;
  }

  .search-box input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  }

  .view-toggle {
    display: flex;
    gap: 10px;
  }

  .view-btn {
    padding: 10px 20px;
    border: 2px solid #e0e0e0;
    background: white;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: 500;
  }

  .view-btn.active {
    background: #667eea;
    color: white;
    border-color: #667eea;
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
    border: none;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    opacity: 0;
    animation: fadeInUp 0.5s ease-out forwards;
  }

  .molecule-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 12px 40px rgba(102, 126, 234, 0.2);
  }

  /* 结构容器 */
  .molecule-card .structure {
    width: 100%;
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border-radius: 12px;
    margin-bottom: 15px;
    position: relative;
    overflow: hidden;
  }

  .molecule-card .structure::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
    animation: pulse 3s ease-in-out infinite;
  }

  .molecule-card .structure svg {
    max-width: 100%;
    max-height: 100%;
    position: relative;
    z-index: 1;
  }

  /* 强制分子结构为纯黑白显示 */
  .molecule-card .structure svg path[stroke]:not([stroke='none']),
  .molecule-card .structure svg ellipse[stroke]:not([stroke='none']) {
    stroke: #000000 !important;
  }

  .molecule-card .structure svg text {
    fill: #000000 !important;
  }

  /* 加载动画 */
  .loading {
    display: inline-block;
    width: 30px;
    height: 30px;
    border: 3px solid rgba(102, 126, 234, 0.3);
    border-top-color: #667eea;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  /* 分子ID标签 */
  .molecule-card .mol-id {
    font-weight: 600;
    color: #333;
    font-family: 'Monaco', 'Menlo', monospace;
    font-size: 1.1em;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top: 10px;
    cursor: pointer;
  }

  .molecule-card .mol-id:hover {
    opacity: 0.8;
  }

  /* 错误提示 */
  .error-msg {
    color: #e74c3c;
    font-size: 0.9em;
    padding: 10px;
    background: #fee;
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

  @keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.3; }
    50% { transform: scale(1.1); opacity: 0.5; }
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
</style>

<!-- 页面内容 -->
<div class="chem-container">
  <div class="header-section">
    <h1>🧪 Compound Library</h1>
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
      <div class="molecule-card" data-id="{{ molecule.ID }}" style="animation-delay: {{ forloop.index | times: 0.05 }}s">
        <div class="structure" data-smiles="{{ molecule.SMILES }}">
          <div class="loading"></div>
        </div>
        <p class="mol-id" title="Click to copy">{{ molecule.ID }}</p>
      </div>
    {% endfor %}
  </div>
</div>

<!-- RDKit库 -->
<script src="https://unpkg.com/@rdkit/rdkit/Code/MinimalLib/dist/RDKit_minimal.js"></script>

<!-- 主脚本 - 优化版 -->
<script>
  // 配置
  const CONFIG = {
    batchSize: 20, // 每批渲染的分子数量
    renderDelay: 50 // 每批之间的延迟（毫秒）
  };

  // 绘制单个分子（纯黑白版本）
  function drawMolecule(holder, RDKit) {
    const smiles = holder.dataset.smiles;
    if (!smiles || !smiles.trim()) return;

    try {
      const mol = RDKit.get_mol(smiles);
      if (mol && mol.is_valid()) {
        // 生成SVG
        const svg = mol.get_svg(200, 200);
        holder.innerHTML = svg;
        
        // 强制所有原子和键显示为黑色
        const svgElement = holder.querySelector('svg');
        if (svgElement) {
          // 将所有带颜色的path和ellipse改为黑色
          const coloredElements = svgElement.querySelectorAll('path[stroke], ellipse[stroke]');
          coloredElements.forEach(el => {
            const stroke = el.getAttribute('stroke');
            if (stroke && stroke !== 'none') {
              el.setAttribute('stroke', '#000000');
            }
            const fill = el.getAttribute('fill');
            if (fill && fill !== 'none' && fill !== '#FFFFFF') {
              el.setAttribute('fill', '#000000');
            }
          });
          
          // 处理文本元素
          const textElements = svgElement.querySelectorAll('text');
          textElements.forEach(el => {
            el.setAttribute('fill', '#000000');
          });
        }
        
        mol.delete();
      } else {
        holder.innerHTML = '<div class="error-msg">Invalid SMILES</div>';
      }
    } catch (e) {
      console.error(`Error rendering: ${smiles}`, e);
      holder.innerHTML = '<div class="error-msg">Render Error</div>';
    }
  }

  // 批量渲染分子（性能优化）
  function renderBatch(molecules, startIndex, RDKit) {
    const endIndex = Math.min(startIndex + CONFIG.batchSize, molecules.length);
    
    for (let i = startIndex; i < endIndex; i++) {
      drawMolecule(molecules[i], RDKit);
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

  // 复制ID到剪贴板
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
    window.RDKit = RDKit;
    console.log('✓ RDKit loaded successfully');

    const initPage = () => {
      const moleculeHolders = document.querySelectorAll('.structure[data-smiles]');
      console.log(`Found ${moleculeHolders.length} molecules`);
      
      // 批量渲染以提高性能
      renderBatch(Array.from(moleculeHolders), 0, RDKit);
      
      // 设置交互功能
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
          <h2 style="color: #e74c3c;">Failed to load RDKit</h2>
          <p>Please refresh the page or check your internet connection</p>
        </div>
      `;
    }
  });
</script>
