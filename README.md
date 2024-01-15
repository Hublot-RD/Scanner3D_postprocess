# Scanner3D_postprocess
Ce répertoire contient le code de traitement des images pour le Scanner 3D.
C'est un complément au projet du Scanner 3D, disponible [ici](https://github.com/GuillaumeChpn/3DScanner).

## Utilisation
1. Dans un éditeur d’image (Paint par exemple), ouvrir l’image fusionnée (son nom termine par *merged*)
2. Rogner l’image pour que l’objet occupe la majeure partie du cadre. Il ne faut pas couper l’objet.
3. Enregistrer l’image et fermer le programme.
4. Ouvrir VS Code et ouvrir le dossier “*Scanner3D_postprocess*”
5. Ouvrir un terminal puis :
    1. Activer l’environnement virtuel: `.\crop_venv\Scripts\activate`
    2. Rogner les images: `python crop.py .\<nom_du_dossier_contennant_les_images>` en remplaçant `<nom_du_dossier_contennant_les_images>` par le chemin d’accès au dossier des images de votre objet.
    3. Quand le programme a terminé, fermer VS Code