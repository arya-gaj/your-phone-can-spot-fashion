"""
Your Phone Can Spot Fashion – A lightweight yet powerful system that analyzes short-form videos in real time to identify fashion products by combining computer vision and natural language processing, all processed locally.

Copyright (C) 2025 Aryaman Gajrani

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Contact: arya-gaj@proton.me
"""

import faiss
from tqdm import tqdm
import os

catalog_dir = "catalog_images"
catalog_image_paths = []
catalog_product_ids = []

for root, _, files in os.walk(catalog_dir):

    for file in files:

        if file.endswith(".jpg") or file.endswith(".png"):
            catalog_image_paths.append(os.path.join(root, file))
            catalog_product_ids.append(os.path.basename(root))
