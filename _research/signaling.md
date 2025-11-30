---
layout: default
title: Research - Cell Signaling Assays
permalink: /research/cell-assays/signaling/
---
<!-- 细胞信号传导实验页面内容 -->

<style>
  /* 基础样式与变量定义 */
  :root {
    --primary: #2563eb;
    --primary-dark: #1d4ed8;
    --primary-light: #eff6ff;
    --secondary: #7c3aed;
    --secondary-light: #f5f3ff;
    --neutral-50: #f8fafc;
    --neutral-100: #f1f5f9;
    --neutral-800: #1e293b;
    --neutral-900: #0f172a;
    --accent: #f97316;
    --success: #10b981;
    --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    --shadow-sm: 0 2px 10px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.12);
    --radius: 12px;
  }

  /* 主容器样式 */
  .signaling-container {
    min-height: 100vh;
    padding: 4rem 1rem;
    max-width: 1400px;
    margin: 0 auto;
    position: relative;
    overflow: hidden;
  }

  /* 背景装饰 */
  .bg-pattern {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
      radial-gradient(var(--primary) 0.5px, transparent 0.5px),
      radial-gradient(var(--primary) 0.5px, var(--neutral-50) 0.5px);
    background-size: 20px 20px;
    background-position: 0 0, 10px 10px;
    opacity: 0.03;
    z-index: 0;
    pointer-events: none;
  }

  /* 标题区域 */
  .section-header {
    text-align: center;
    margin-bottom: 6rem;
    position: relative;
    z-index: 1;
  }

  .section-title {
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    background-image: linear-gradient(135deg, var(--primary), var(--secondary));
    margin-bottom: 1.5rem;
    letter-spacing: -0.02em;
    position: relative;
    display: inline-block;
  }

  .section-title::after {
    content: '';
    position: absolute;
    bottom: -12px;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 4px;
    background: var(--accent);
    border-radius: 2px;
    opacity: 0;
    transform-origin: center;
    transform: translate(-50%, 10px);
    transition: var(--transition);
  }

  .section-header:hover .section-title::after {
    opacity: 1;
    transform: translate(-50%, 0);
  }

  .section-subtitle {
    font-size: clamp(1.1rem, 2vw, 1.3rem);
    color: var(--neutral-800);
    max-width: 700px;
    margin: 0 auto;
    line-height: 1.6;
    opacity: 0.8;
  }

  /* 内容网格布局 */
  .content-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    margin-bottom: 6rem;
    position: relative;
    z-index: 1;
  }

  @media (max-width: 900px) {
    .content-grid {
      grid-template-columns: 1fr;
    }
  }

  /* 特性卡片 */
  .feature-card {
    background: white;
    border-radius: var(--radius);
    padding: 2.5rem;
    box-shadow: var(--shadow-md);
    transition: var(--transition);
    border: 1px solid transparent;
    overflow: hidden;
    position: relative;
    cursor: pointer;
  }

  .feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary-light));
    opacity: 0;
    transition: var(--transition);
    z-index: -1;
  }

  .feature-card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-lg);
    border-color: rgba(37, 99, 235, 0.1);
  }

  .feature-card:hover::before {
    opacity: 1;
  }

  .feature-icon {
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background: var(--primary-light);
    color: var(--primary);
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    transition: var(--transition);
  }

  .feature-card:hover .feature-icon {
    background: var(--primary);
    color: white;
    transform: scale(1.1);
  }

  .feature-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--neutral-900);
    margin-bottom: 1rem;
    transition: var(--transition);
  }

  .feature-card:hover .feature-title {
    color: var(--primary);
  }

  .feature-desc {
    color: var(--neutral-800);
    line-height: 1.7;
    margin-bottom: 1.5rem;
    opacity: 0.85;
  }

  .feature-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--primary);
    font-weight: 600;
    text-decoration: none;
    transition: var(--transition);
  }

  .feature-link svg {
    width: 16px;
    height: 16px;
    transition: var(--transition);
  }

  .feature-card:hover .feature-link {
    color: var(--primary-dark);
  }

  .feature-card:hover .feature-link svg {
    transform: translateX(5px);
  }

  /* 通路研究部分 */
  .pathways-section {
    margin: 8rem 0;
    position: relative;
    z-index: 1;
  }

  .pathways-header {
    margin-bottom: 3rem;
    text-align: center;
  }

  .pathways-title {
    font-size: clamp(1.8rem, 3vw, 2.5rem);
    font-weight: 700;
    color: var(--neutral-900);
    margin-bottom: 1rem;
  }

  .pathways-subtitle {
    color: var(--neutral-800);
    max-width: 700px;
    margin: 0 auto;
    opacity: 0.8;
  }

  .pathways-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1.5rem;
  }

  .pathway-item {
    background: white;
    border-radius: var(--radius);
    padding: 1.5rem;
    text-align: center;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
    position: relative;
    overflow: hidden;
  }

  .pathway-item::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: var(--primary);
    transform: scaleX(0);
    transition: var(--transition);
  }

  .pathway-item:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
  }

  .pathway-item:hover::after {
    transform: scaleX(1);
  }

  .pathway-item strong {
    color: var(--neutral-900);
    transition: var(--transition);
  }

  .pathway-item:hover strong {
    color: var(--primary);
  }

  /* 应用领域 */
  .applications-section {
    margin: 6rem 0;
    padding: 3rem;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary-light));
    border-radius: var(--radius);
    position: relative;
    z-index: 1;
  }

  .applications-title {
    font-size: clamp(1.5rem, 3vw, 2rem);
    font-weight: 700;
    color: var(--neutral-900);
    margin-bottom: 2rem;
  }

  .applications-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
  }

  .application-item {
    display: flex;
    gap: 1rem;
    align-items: flex-start;
  }

  .application-icon {
    width: 24px;
    height: 24px;
    flex-shrink: 0;
    color: var(--primary);
    margin-top: 3px;
  }

  .application-text {
    color: var(--neutral-800);
    line-height: 1.6;
  }

  /* 交互按钮 */
  .action-buttons {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 6rem;
    position: relative;
    z-index: 1;
  }

  .btn {
    padding: 14px 30px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    gap: 8px;
    border: none;
    cursor: pointer;
    font-size: 1rem;
  }

  .btn-primary {
    background: var(--primary);
    color: white;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
  }

  .btn-primary:hover {
    background: var(--primary-dark);
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
  }

  .btn-outline {
    background: transparent;
    color: var(--primary);
    border: 1px solid var(--primary);
  }

  .btn-outline:hover {
    background: var(--primary-light);
    transform: translateY(-3px);
  }

  /* 动画效果 */
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .animate-on-scroll {
    opacity: 0;
    animation: fadeInUp 0.6s forwards;
    animation-play-state: paused;
  }

  .animate-on-scroll.visible {
    animation-play-state: running;
  }

  /* 延迟动画 */
  .delay-1 { animation-delay: 0.1s; }
  .delay-2 { animation-delay: 0.2s; }
  .delay-3 { animation-delay: 0.3s; }
  .delay-4 { animation-delay: 0.4s; }
  .delay-5 { animation-delay: 0.5s; }
  .delay-6 { animation-delay: 0.6s; }
</style>

<div class="signaling-container">
  <!-- 背景装饰 -->
  <div class="bg-pattern"></div>
  
  <!-- 标题区域 -->
  <div class="section-header animate-on-scroll">
    <h1 class="section-title">Cell Signaling Assays</h1>
    <p class="section-subtitle">Advanced systems for decoding cellular communication networks and their role in disease pathways</p>
  </div>
  
  <!-- 核心特性 -->
  <div class="content-grid">
    <div class="feature-card animate-on-scroll delay-1">
      <div class="feature-icon">📊</div>
      <h3 class="feature-title">Reporter Gene Assays</h3>
      <p class="feature-desc">Dual-luciferase and GFP-based reporter systems to quantify pathway activation downstream of key receptors and transcription factors with high precision.</p>
      <a href="#" class="feature-link">
        Learn more
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </a>
    </div>
    
    <div class="feature-card animate-on-scroll delay-2">
      <div class="feature-icon">🔬</div>
      <h3 class="feature-title">Phosphoprotein Analysis</h3>
      <p class="feature-desc">High-sensitivity ELISA and Western blot protocols to measure protein phosphorylation events at critical signaling nodes with subcellular resolution.</p>
      <a href="#" class="feature-link">
        Learn more
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </a>
    </div>
    
    <div class="feature-card animate-on-scroll delay-3">
      <div class="feature-icon">📈</div>
      <h3 class="feature-title">Dose-Response Profiling</h3>
      <p class="feature-desc">Automated liquid handling and detection to generate precise EC50/IC50 curves for pathway modulation with enhanced data reproducibility.</p>
      <a href="#" class="feature-link">
        Learn more
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </a>
    </div>
    
    <div class="feature-card animate-on-scroll delay-4">
      <div class="feature-icon">🔄</div>
      <h3 class="feature-title">Kinase Activity Assays</h3>
      <p class="feature-desc">Target-specific kinase assays to identify direct modulators of key signaling enzymes in disease pathways with high-throughput capabilities.</p>
      <a href="#" class="feature-link">
        Learn more
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </a>
    </div>
  </div>
  
  <!-- 重点研究的通路 -->
  <div class="pathways-section animate-on-scroll delay-1">
    <div class="pathways-header">
      <h2 class="pathways-title">Key Pathways Under Investigation</h2>
      <p class="pathways-subtitle">Our research focuses on critical signaling networks involved in disease progression and therapeutic intervention</p>
    </div>
    
    <div class="pathways-grid">
      <div class="pathway-item animate-on-scroll delay-2">
        <strong>NF-κB Signaling</strong>
      </div>
      <div class="pathway-item animate-on-scroll delay-3">
        <strong>JAK-STAT Pathway</strong>
      </div>
      <div class="pathway-item animate-on-scroll delay-4">
        <strong>MAPK/ERK Cascade</strong>
      </div>
      <div class="pathway-item animate-on-scroll delay-5">
        <strong>PI3K/Akt/mTOR Axis</strong>
      </div>
      <div class="pathway-item animate-on-scroll delay-6">
        <strong>Type I Interferon Response</strong>
      </div>
      <div class="pathway-item animate-on-scroll delay-1">
        <strong>Apoptosis Signaling</strong>
      </div>
    </div>
  </div>
  
  <!-- 应用领域 -->
  <div class="applications-section animate-on-scroll delay-2">
    <h2 class="applications-title">Primary Applications</h2>
    <div class="applications-list">
      <div class="application-item">
        <div class="application-icon">•</div>
        <div class="application-text">Identifying pathway-selective modulators for targeted therapeutics development</div>
      </div>
      <div class="application-item">
        <div class="application-icon">•</div>
        <div class="application-text">Mechanism of action studies to understand compound interactions</div>
      </div>
      <div class="application-item">
        <div class="application-icon">•</div>
        <div class="application-text">Structure-activity relationship (SAR) development for optimized efficacy</div>
      </div>
      <div class="application-item">
        <div class="application-icon">•</div>
        <div class="application-text">Profiling compound selectivity across related signaling networks</div>
      </div>
      <div class="application-item">
        <div class="application-icon">•</div>
        <div class="application-text">Disease modeling through pathway dysregulation analysis</div>
      </div>
      <div class="application-item">
        <div class="application-icon">•</div>
        <div class="application-text">Biomarker identification for drug response prediction</div>
      </div>
    </div>
  </div>
  
  <!-- 操作按钮 -->
  <div class="action-buttons animate-on-scroll delay-3">
    <a href="{{ '/research/cell-assays/' | relative_url }}" class="btn btn-outline">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"/>
      </svg>
      Back to Cellular Assays
    </a>
    <a href="#" class="btn btn-primary">
      Request Assay Details
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
        <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
        <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>
      </svg>
    </a>
  </div>
</div>

<script>
  // 滚动动画效果
  document.addEventListener('DOMContentLoaded', function() {
    // 检测元素是否在视口中
    const isElementInViewport = (el) => {
      const rect = el.getBoundingClientRect();
      return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.85 &&
        rect.bottom >= 0
      );
    };

    // 处理滚动动画
    const handleScrollAnimation = () => {
      const animatedElements = document.querySelectorAll('.animate-on-scroll');
      
      animatedElements.forEach(element => {
        if (isElementInViewport(element) && !element.classList.contains('visible')) {
          element.classList.add('visible');
        }
      });
    };

    // 初始检查
    handleScrollAnimation();
    
    // 滚动时检查
    window.addEventListener('scroll', handleScrollAnimation);
    
    // 窗口大小改变时检查
    window.addEventListener('resize', handleScrollAnimation);
  });
</script>