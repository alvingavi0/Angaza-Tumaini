#!/usr/bin/env python3
"""Surgical update of team member cards using manual replacements"""

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and replace the team section
output_lines = []
i = 0
replacements_made = 0

while i < len(lines):
    line = lines[i]
    
    # Look for "Meet our Team" heading
    if 'Meet our Team' in line and '<h3' in line:
        # Found team section - output until we find team cards
        output_lines.append(line)
        i += 1
        
        # Collect lines until we hit first grid
        while i < len(lines) and 'grid grid-cols-1 md:grid-cols-2' not in lines[i]:
            output_lines.append(lines[i])
            i += 1
        
        # Now we're at the 2-col grid opening
        if i < len(lines):
            output_lines.append(lines[i])  # Add grid opening
            i += 1
            
            # Skip the first article and its content (Erick/Krista)
            article_count = 0
            while i < len(lines) and article_count < 2:
                if '<article' in lines[i]:
                    article_count += 1
                    # Skip until closing </article>
                    while i < len(lines) and '</article>' not in lines[i]:
                        i += 1
                    if i < len(lines):
                        i += 1  # Skip closing </article>
                
                # Skip whitespace between articles
                while i < len(lines) and lines[i].strip() == '':
                    i += 1
            
            # Now output new flip cards
            # Erick/Krista card
            output_lines.append('                        <article class="team-member rounded-xl shadow-md scroll-reveal">\n')
            output_lines.append('                            <div class="team-member-inner">\n')
            output_lines.append('                                <div class="team-member-front rounded-xl">\n')
            output_lines.append('                                    <img src="filez/eric-and-krista.jfif" alt="Erick and Krista Baraza" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src=\'https://placehold.co/160x160?text=Erick+%26+Krista\'">\n')
            output_lines.append('                                    <h4 class="text-lg font-bold">Erick & Krista</h4>\n')
            output_lines.append('                                    <p class="text-sm text-gray-600">Founders & Missionaries</p>\n')
            output_lines.append('                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>\n')
            output_lines.append('                                </div>\n')
            output_lines.append('                                <div class="team-member-back rounded-xl">\n')
            output_lines.append('                                    <h4 class="text-lg font-bold mb-1">Erick & Krista Baraza</h4>\n')
            output_lines.append('                                    <div class="role text-sm mb-2">Founders & Missionaries</div>\n')
            output_lines.append('                                    <p class="text-sm mb-2">Passionate missionaries and founders of Angaza Tumaini, bringing hope and transformation to Kibera through the Gospel.</p>\n')
            output_lines.append('                                    <div class="quote text-xs">"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</div>\n')
            output_lines.append('                                </div>\n')
            output_lines.append('                            </div>\n')
            output_lines.append('                        </article>\n')
            output_lines.append('\n')
            
            # Evans card
            output_lines.append('                        <article class="team-member rounded-xl shadow-md scroll-reveal">\n')
            output_lines.append('                            <div class="team-member-inner">\n')
            output_lines.append('                                <div class="team-member-front rounded-xl">\n')
            output_lines.append('                                    <img src="filez/hypeman.jpg" alt="Evans Wandera" class="w-40 h-40 rounded-full object-cover shadow-lg mb-4" onerror="this.onerror=null;this.src=\'https://placehold.co/160x160?text=Evans\'">\n')
            output_lines.append('                                    <h4 class="text-lg font-bold">Evans Wandera</h4>\n')
            output_lines.append('                                    <p class="text-sm text-gray-600">Programs Coordinator</p>\n')
            output_lines.append('                                    <p class="text-xs text-gray-500 mt-4">Hover to flip →</p>\n')
            output_lines.append('                                </div>\n')
            output_lines.append('                                <div class="team-member-back rounded-xl">\n')
            output_lines.append('                                    <h4 class="text-lg font-bold mb-1">Evans Wandera</h4>\n')
            output_lines.append('                                    <div class="role text-sm mb-2">Programs Coordinator</div>\n')
            output_lines.append('                                    <p class="text-sm mb-2">Passionate about serving his community, ensuring every child receives care, mentorship, and academic support with Christ-centered love.</p>\n')
            output_lines.append('                                    <div class="quote text-xs">"Train up a child in the way he should go, and when he is old, he will not depart from it." – Proverbs 22:6</div>\n')
            output_lines.append('                                </div>\n')
            output_lines.append('                            </div>\n')
            output_lines.append('                        </article>\n')
            output_lines.append('                    </div>\n')
            
            replacements_made += 1
            print(f"✅ Updated 2-column grid at line {i}")
    else:
        output_lines.append(line)
        i += 1

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(output_lines)

print(f"✅ Replacements made: {replacements_made}")
