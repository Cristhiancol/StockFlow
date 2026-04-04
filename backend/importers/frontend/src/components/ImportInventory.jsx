# 1. Ir a carpeta
cd StockFlow

# 2. Crear carpetas
mkdir -p backend/importers
mkdir -p frontend/src/components

# 3. Crear archivo Python
cat > backend/importers/mainsaver_importer.py << 'EOF'
[PEGA EL CÓDIGO PYTHON ARRIBA]
EOF

# 4. Git
git add backend/
git commit -m "Add MainSaver importer"
git push origin main
