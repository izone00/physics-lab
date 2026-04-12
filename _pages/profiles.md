---
layout: page
permalink: /people/
title: People
description: Members of the Nuclear Physics Laboratory at Yonsei University.
nav: true
nav_order: 2
---

<style>
.people-section { margin-bottom: 3rem; }
.people-section h3 {
  border-bottom: 3px solid var(--global-theme-color);
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
  font-size: 1.4rem;
  font-weight: 700;
}

/* Flexbox Grid for centering and wrapping */
.people-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  align-items: stretch; /* Ensure equal height */
}

/* Card Design */
.person-card {
  background: var(--global-card-bg-color);
  border: 1px solid var(--global-divider-color);
  border-radius: 6px;
  padding: 1.5rem 1rem;
  text-align: center;
  transition: box-shadow 0.2s ease, transform 0.2s ease;
  flex: 0 1 230px;
  display: flex;
  flex-direction: column;
  width: 100%;
}
.person-card:hover { 
  box-shadow: 0 8px 24px rgba(0,0,0,0.15); 
  transform: translateY(-3px);
}
.person-avatar {
  width: 90px; height: 90px;
  border-radius: 12px;
  background: var(--global-divider-color);
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 1rem;
  font-size: 2.2rem; color: var(--global-theme-color);
  overflow: hidden;
}
.person-name { 
  font-weight: 800; /* High contrast */
  font-size: 1.1rem; 
  margin-bottom: 0.2rem; 
  color: var(--global-text-color);
}
.person-title { 
  font-size: 0.85rem; 
  font-weight: 500;
  color: var(--global-text-color-light); 
  margin-bottom: 0.5rem; 
}
.person-interests {
  font-size: 0.75rem;
  color: var(--global-text-color-light);
  opacity: 0.85;
  margin-bottom: 1rem;
  flex-grow: 1; /* Pushes the email to the bottom */
}
.person-email { 
  font-size: 0.8rem; 
  word-break: break-all; 
  margin-top: auto; /* Always stay at the bottom */
}
.person-email a { 
  color: var(--global-theme-color); 
  font-weight: 600;
  text-decoration: none;
}
.person-email a:hover { text-decoration: underline; }

/* Faculty PI Horizontal Card */
.pi-card {
  display: flex;
  background: var(--global-card-bg-color);
  border: 1px solid var(--global-divider-color);
  border-radius: 6px;
  padding: 2rem;
  gap: 2rem;
  align-items: center;
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.pi-card:hover {
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  transform: translateY(-3px);
}
.pi-avatar {
  flex-shrink: 0;
  width: 130px; height: 130px;
  border-radius: 12px;
  background: var(--global-divider-color);
  display: flex; align-items: center; justify-content: center;
  font-size: 4rem; color: var(--global-theme-color);
}
.pi-info {
  flex-grow: 1;
}
.pi-name { 
  font-weight: 800; 
  font-size: 1.6rem; 
  margin-bottom: 0.2rem; 
  color: var(--global-text-color); 
}
.pi-title { 
  font-size: 1rem; 
  font-weight: 500; 
  color: var(--global-text-color-light); 
  margin-bottom: 0.5rem; 
}
.pi-interests { 
  font-size: 0.9rem; 
  color: var(--global-text-color-light); 
  margin-bottom: 1rem; 
}
.pi-contact { 
  font-size: 0.9rem; 
  margin-bottom: 1rem; 
  line-height: 1.6;
}
.pi-contact a { 
  color: var(--global-theme-color); 
  font-weight: 600; 
  text-decoration: none;
}
.pi-contact a:hover { text-decoration: underline; }
.pi-contact i {
  width: 1.2rem;
  text-align: center;
  margin-right: 0.3rem;
  color: var(--global-text-color-light);
}

.pi-socials {
  display: flex;
  gap: 1rem;
  font-size: 1.4rem;
}
.pi-socials a {
  color: var(--global-text-color-light);
  transition: color 0.2s;
}
.pi-socials a:hover {
  color: var(--global-theme-color);
}

@media (max-width: 650px) {
  .pi-card {
    flex-direction: column;
    text-align: center;
    padding: 1.5rem;
    gap: 1rem;
  }
  .pi-socials {
    justify-content: center;
  }
}
</style>

<div class="people-section">
  <h3>Faculty</h3>
  <div class="pi-card">
    <div class="pi-avatar">👨‍🔬</div>
    <div class="pi-info">
      <div class="pi-name">LIM, SangHoon</div>
      <div class="pi-title">Associate Professor</div>
      <div class="pi-interests">High Energy Nuclear Physics, Quark-Gluon Plasma</div>
      <div class="pi-contact">
        <i class="fa-solid fa-envelope"></i> <a href="mailto:shlim@pusan.ac.kr">shlim@pusan.ac.kr</a><br>
        <i class="fa-solid fa-phone"></i> 051-510-7731
      </div>
      <div class="pi-socials">
        <a href="#" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
        <a href="#" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
      </div>
    </div>
  </div>
</div>

<div class="people-section">
  <h3>Research Professors & Postdoctoral Researchers</h3>
  <div class="people-grid">
    <div class="person-card">
      <div class="person-avatar">🔬</div>
      <div class="person-name">BOK, JeongSu</div>
      <div class="person-title">Research Professor</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">🔬</div>
      <div class="person-name">KIM, Chong</div>
      <div class="person-title">Postdoctoral Researcher</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">🔬</div>
      <div class="person-name">DANISCH, Meike</div>
      <div class="person-title">Postdoctoral Researcher</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">🔬</div>
      <div class="person-name">SMITH, Krista</div>
      <div class="person-title">Postdoctoral Researcher</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">🔬</div>
      <div class="person-name">LEE, JongWon</div>
      <div class="person-title">Postdoctoral Researcher</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">🔬</div>
      <div class="person-name">PARK, JongHan</div>
      <div class="person-title">Visiting Researcher</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
  </div>
</div>

<div class="people-section">
  <h3>Graduate Students (PhD)</h3>
  <div class="people-grid">
    <div class="person-card">
      <div class="person-avatar">🎓</div>
      <div class="person-name">RYU, JaeHyeok</div>
      <div class="person-title">PhD Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">🎓</div>
      <div class="person-name">JI, SuJeong</div>
      <div class="person-title">PhD Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">🎓</div>
      <div class="person-name">LIM, HyunJi</div>
      <div class="person-title">PhD Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">🎓</div>
      <div class="person-name">OH, JongHo</div>
      <div class="person-title">PhD Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
  </div>
</div>

<div class="people-section">
  <h3>Graduate Students (Master)</h3>
  <div class="people-grid">
    <div class="person-card">
      <div class="person-avatar">📚</div>
      <div class="person-name">CHOI, ChangHwan</div>
      <div class="person-title">Master Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">📚</div>
      <div class="person-name">HONG, YoonHa</div>
      <div class="person-title">Master Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">📚</div>
      <div class="person-name">KIM, MinJae</div>
      <div class="person-title">Master Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">📚</div>
      <div class="person-name">PARK, JinHyun</div>
      <div class="person-title">Master Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
    <div class="person-card">
      <div class="person-avatar">📚</div>
      <div class="person-name">JEONG, SeulI</div>
      <div class="person-title">Master Student</div>
      <div class="person-interests">Nuclear Physics</div>
      <div class="person-email"></div>
    </div>
  </div>
</div>
