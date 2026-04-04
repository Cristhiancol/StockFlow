"""
Script para importar datos de inventario desde CSV/Excel
Origen: MainSaver - Descarga diaria de inventario
Estilo: Cyberpunk 🌐💜
"""

import pandas as pd
import json
from datetime import datetime
import sys

class InventoryImporter:
    def __init__(self):
        self.data = None
        self.processed_data = {
            'productos': [],
            'inventario': [],
            'proveedores': set(),
            'errors': []
        }
    
    def load_csv(self, file_path: str):
        """Cargar datos desde CSV de MainSaver"""
        try:
            self.data = pd.read_csv(file_path, encoding='utf-8-sig', sep='\t')
            print(f"✅ Archivo cargado: {len(self.data)} registros")
            return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def clean_currency(self, value):
        """Limpiar valores monetarios"""
        if pd.isna(value):
            return 0
        value_str = str(value).replace('$', '').replace(',', '').strip()
        try:
            return float(value_str)
        except:
            return 0
    
    def process_data(self):
        """Procesar datos del inventario"""
        if self.data is None:
            return False
        
        for idx, row in self.data.iterrows():
            try:
                referencia = str(row['REFERENCIA']).strip()
                descripcion = str(row['DESCRIPCION']).strip()
                nit_proveedor = str(row['NIT PROVEEDOR']).strip()
                bodega = str(row['BODEGA']).strip()
                
                producto = {
                    'id': idx + 1,
                    'codigo_interno': referencia,
                    'nombre': descripcion,
                    'proveedor_nit': nit_proveedor,
                    'unidad_medida': str(row.get('UM EMISION', 'UND')).strip(),
                    'clasificacion_abc': str(row.get('CLASE ABC', 'C')).strip(),
                    'valor_unitario': self.clean_currency(row['COSTO UNITARIO']),
                    'cantidad_minima': int(row.get('PUNTO PEDIDO', 0)) or int(row.get('MINIMO', 0)),
                }
                
                inventario = {
                    'producto_id': idx + 1,
                    'cantidad_actual': int(row.get('STOCK ACTUAL', 0)),
                    'ubicacion': bodega,
                }
                
                self.processed_data['productos'].append(producto)
                self.processed_data['inventario'].append(inventario)
                self.processed_data['proveedores'].add(nit_proveedor)
                
            except Exception as e:
                self.processed_data['errors'].append({'row': idx + 2, 'error': str(e)})
        
        return True
    
    def export_json(self, file_path: str):
        """Exportar datos a JSON"""
        try:
            export_data = {
                'metadata': {
                    'fecha_importacion': datetime.now().isoformat(),
                    'total_productos': len(self.processed_data['productos']),
                    'total_proveedores': len(self.processed_data['proveedores']),
                },
                'productos': self.processed_data['productos'],
                'inventario': self.processed_data['inventario'],
                'proveedores': list(self.processed_data['proveedores']),
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ JSON exportado a: {file_path}")
            return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        importer = InventoryImporter()
        if importer.load_csv(csv_file):
            if importer.process_data():
                json_output = csv_file.replace('.csv', '_processed.json')
                importer.export_json(json_output)
    else:
        print("Uso: python mainsaver_importer.py <archivo.csv>")
