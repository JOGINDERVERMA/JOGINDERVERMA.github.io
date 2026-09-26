css_addition = """
/* Skills */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 4rem;
}

.skill-category h3 {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border-color);
}

.skill-list {
    list-style: none;
}

.skill-list li {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}

.skill-list li::before {
    content: '—';
    margin-right: 10px;
    color: var(--text-primary);
    font-weight: 600;
}
"""

with open('css/style.css', 'a') as f:
    f.write(css_addition)
