// JavaScript spécifique aux articles
document.addEventListener('DOMContentLoaded', function() {
    // Estimation du temps de lecture
    const content = document.querySelector('.article-content, .content');
    if (content) {
        const wordsPerMinute = 200;
        const textContent = content.textContent || content.innerText;
        const wordCount = textContent.trim().split(/\s+/).length;
        const readingTime = Math.ceil(wordCount / wordsPerMinute);
        
        addReadingTime(readingTime);
    }

    // Amélioration des liens dans le contenu
    enhanceContentLinks();

    // Table des matières automatique pour les longs articles
    generateTableOfContents();

    // Partage social (simulation)
    addSocialShareButtons();
});

function addReadingTime(minutes) {
    const meta = document.querySelector('.article-meta');
    if (meta) {
        const readingTimeElement = document.createElement('span');
        readingTimeElement.className = 'reading-time';
        readingTimeElement.innerHTML = `<i>📖 ${minutes} min de lecture</i>`;
        readingTimeElement.style.cssText = `
            display: block;
            margin-top: 5px;
            font-size: 0.8em;
            color: #6c757d;
        `;
        meta.appendChild(readingTimeElement);
    }
}

function enhanceContentLinks() {
    const contentLinks = document.querySelectorAll('.article-content a, .content a');
    contentLinks.forEach(link => {
        if (link.hostname && link.hostname !== window.location.hostname) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
            link.title = 'Lien externe - Ouvre dans un nouvel onglet';
        }
    });
}

function generateTableOfContents() {
    const content = document.querySelector('.article-content, .content');
    const headings = content ? content.querySelectorAll('h2, h3, h4') : [];
    
    if (headings.length > 2) {
        const toc = document.createElement('div');
        toc.className = 'table-of-contents';
        toc.style.cssText = `
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            border-left: 4px solid #007bff;
        `;
        
        const tocTitle = document.createElement('h3');
        tocTitle.textContent = 'Table des matières';
        tocTitle.style.marginTop = '0';
        toc.appendChild(tocTitle);
        
        const tocList = document.createElement('ul');
        tocList.style.cssText = 'list-style-type: none; padding-left: 0;';
        
        headings.forEach((heading, index) => {
            const id = `heading-${index}`;
            heading.id = id;
            
            const listItem = document.createElement('li');
            listItem.style.marginBottom = '5px';
            
            const link = document.createElement('a');
            link.href = `#${id}`;
            link.textContent = heading.textContent;
            link.style.cssText = `
                text-decoration: none;
                color: #495057;
                padding: 2px 0;
                display: block;
            `;
            link.addEventListener('mouseover', () => link.style.color = '#007bff');
            link.addEventListener('mouseout', () => link.style.color = '#495057');
            
            listItem.appendChild(link);
            tocList.appendChild(listItem);
        });
        
        toc.appendChild(tocList);
        content.parentNode.insertBefore(toc, content);
    }
}

function addSocialShareButtons() {
    const articleTitle = document.querySelector('h1');
    if (articleTitle) {
        const shareContainer = document.createElement('div');
        shareContainer.className = 'social-share';
        shareContainer.style.cssText = `
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e9ecef;
            text-align: center;
        `;
        
        const shareTitle = document.createElement('p');
        shareTitle.textContent = 'Partager cet article :';
        shareTitle.style.marginBottom = '15px';
        shareContainer.appendChild(shareTitle);
        
        const shareButtons = [
            { name: 'Twitter', color: '#1da1f2', icon: '🐦' },
            { name: 'Facebook', color: '#3b5998', icon: '📘' },
            { name: 'LinkedIn', color: '#0077b5', icon: '💼' }
        ];
        
        shareButtons.forEach(button => {
            const btn = document.createElement('button');
            btn.innerHTML = `${button.icon} ${button.name}`;
            btn.style.cssText = `
                background-color: ${button.color};
                color: white;
                border: none;
                padding: 8px 15px;
                margin: 0 5px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 0.9em;
                transition: transform 0.2s ease;
            `;
            btn.addEventListener('mouseover', () => btn.style.transform = 'scale(1.05)');
            btn.addEventListener('mouseout', () => btn.style.transform = 'scale(1)');
            btn.addEventListener('click', () => {
                alert(`Partage sur ${button.name} (fonctionnalité de démonstration)`);
            });
            shareContainer.appendChild(btn);
        });
        
        const content = document.querySelector('.content, .article-content');
        if (content) {
            content.parentNode.insertBefore(shareContainer, content.nextSibling);
        }
    }
}
