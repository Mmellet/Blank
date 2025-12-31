#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour renommer les fichiers markdown selon leurs titres
comme dans le dossier meditions
"""

import os
import re
import yaml
from pathlib import Path
from unicodedata import normalize

def slugify(text):
    """
    Convertit un texte en slug (comme dans meditions)
    Exemple: "Manifeste des petites mains" -> "manifeste-des-petites-mains"
    """
    # Normaliser les caractères Unicode (é -> e, etc.)
    text = normalize('NFKD', text)
    
    # Convertir en minuscules
    text = text.lower()
    
    # Remplacer les caractères spéciaux par des espaces ou les supprimer
    # Garder les lettres, chiffres, espaces et tirets
    text = re.sub(r'[^\w\s-]', '', text)
    
    # Remplacer les espaces multiples et tirets par un seul tiret
    text = re.sub(r'[-\s]+', '-', text)
    
    # Supprimer les tirets en début et fin
    text = text.strip('-')
    
    return text

def extract_title_from_frontmatter(file_path):
    """
    Extrait le titre du frontmatter YAML d'un fichier markdown
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si le fichier commence par ---
        if not content.startswith('---'):
            return None
        
        # Extraire le frontmatter (entre les deux ---)
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None
        
        frontmatter_text = parts[1]
        
        # Parser le YAML
        try:
            frontmatter = yaml.safe_load(frontmatter_text)
            if frontmatter and 'title' in frontmatter:
                return frontmatter['title']
        except yaml.YAMLError:
            return None
        
    except Exception as e:
        print(f"Erreur lors de la lecture de {file_path}: {e}")
        return None
    
    return None

def rename_files_in_directory(directory):
    """
    Renomme tous les fichiers markdown dans un répertoire selon leurs titres
    """
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"Le répertoire {directory} n'existe pas")
        return
    
    renamed_count = 0
    skipped_count = 0
    
    # Parcourir tous les fichiers .md sauf _index.md
    for file_path in dir_path.glob('*.md'):
        if file_path.name == '_index.md':
            continue
        
        # Extraire le titre
        title = extract_title_from_frontmatter(file_path)
        
        if not title:
            print(f"⚠️  Pas de titre trouvé dans {file_path.name}")
            skipped_count += 1
            continue
        
        # Générer le nouveau nom de fichier
        new_name = slugify(title) + '.md'
        new_path = dir_path / new_name
        
        # Vérifier si le fichier a déjà le bon nom
        if file_path.name == new_name:
            print(f"✓ {file_path.name} a déjà le bon nom")
            continue
        
        # Vérifier si le nouveau nom existe déjà
        if new_path.exists() and new_path != file_path:
            print(f"⚠️  Le fichier {new_path.name} existe déjà, on garde {file_path.name}")
            skipped_count += 1
            continue
        
        # Renommer le fichier
        try:
            file_path.rename(new_path)
            print(f"✓ {file_path.name} -> {new_name}")
            renamed_count += 1
        except Exception as e:
            print(f"❌ Erreur lors du renommage de {file_path.name}: {e}")
            skipped_count += 1
    
    print(f"\n📊 Résumé pour {directory}:")
    print(f"   - {renamed_count} fichier(s) renommé(s)")
    print(f"   - {skipped_count} fichier(s) ignoré(s)")

def main():
    """
    Fonction principale
    """
    base_dir = Path(__file__).parent
    content_dir = base_dir / 'content'
    
    # Dossiers à traiter
    directories = [
        content_dir / 'carnet',
        content_dir / 'creations',
        content_dir / 'petites',
    ]
    
    print("🔄 Renommage des fichiers selon leurs titres...\n")
    
    for directory in directories:
        print(f"\n📁 Traitement de {directory.name}/")
        print("-" * 50)
        rename_files_in_directory(directory)
    
    print("\n✅ Terminé!")

if __name__ == '__main__':
    main()

