Found 5 chunks.json files:
  - /kaggle/working/_repo_tmp/output/phase1-extracted/Physique-lois-de-newton-cours-Exercices/chunks.json
  - /kaggle/working/_repo_tmp/output/phase1-extracted/Maths-fonctions-cours/chunks.json
  - /kaggle/working/_repo_tmp/output/phase1-extracted/Maths-fonctions-corrige-serie-d-exercices/chunks.json
  - /kaggle/working/_repo_tmp/output/phase1-extracted/English-examen/chunks.json
  - /kaggle/working/_repo_tmp/output/phase1-extracted/English-cours/chunks.json

Split sizes:
  Physique_Chimie_2Bac: 34 chunks
  Mathématiques_2Bac: 153 chunks
  English_2Bac: 1083 chunks

DatasetDict: DatasetDict({
    Physique_Chimie_2Bac: Dataset({
        features: ['chunk_id', 'source_file', 'page_number', 'subject', 'level', 'language', 'specialization', 'chapter', 'section_title', 'content_type', 'content', 'math_formulas', 'char_count'],
        num_rows: 34
    })
    Mathématiques_2Bac: Dataset({
        features: ['chunk_id', 'source_file', 'page_number', 'subject', 'level', 'language', 'specialization', 'chapter', 'section_title', 'content_type', 'content', 'math_formulas', 'char_count'],
        num_rows: 153
    })
    English_2Bac: Dataset({
        features: ['chunk_id', 'source_file', 'page_number', 'subject', 'level', 'language', 'specialization', 'chapter', 'section_title', 'content_type', 'content', 'math_formulas', 'char_count'],
        num_rows: 1083
    })
})
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/tmp/ipykernel_58/2836990061.py in <cell line: 0>()
     48 # 5. Push ALL splits at once in a single call (no overwriting!)
     49 HUB_DATASET = "Saad-Elouakate/AI-Adaptive-Learning"
---> 50 dataset_dict.push_to_hub(HUB_DATASET)
     51 print(f"\n✅ All splits pushed to: https://huggingface.co/datasets/{HUB_DATASET}")

/usr/local/lib/python3.12/dist-packages/datasets/dataset_dict.py in push_to_hub(self, repo_id, config_name, set_default, data_dir, commit_message, commit_description, private, token, revision, create_pr, max_shard_size, num_shards, embed_external_files, num_proc)
   1747 
   1748         self._check_values_type()
-> 1749         self._check_values_features()
   1750         if config_name == "data":
   1751             raise ValueError("`config_name` cannot be 'data'. Please, choose another name for configuration.")

/usr/local/lib/python3.12/dist-packages/datasets/dataset_dict.py in _check_values_features(self)
     73         for item_a, item_b in zip(items[:-1], items[1:]):
     74             if item_a[1].features != item_b[1].features:
---> 75                 raise ValueError(
     76                     f"All datasets in `DatasetDict` should have the same features but features for '{item_a[0]}' and '{item_b[0]}' don't match: {item_a[1].features} != {item_b[1].features}"
     77                 )

ValueError: All datasets in `DatasetDict` should have the same features but features for 'Mathématiques_2Bac' and 'English_2Bac' don't match: {'chunk_id': Value('string'), 'source_file': Value('string'), 'page_number': Value('int64'), 'subject': Value('string'), 'level': Value('string'), 'language': Value('string'), 'specialization': Value('string'), 'chapter': Value('string'), 'section_title': Value('string'), 'content_type': Value('string'), 'content': Value('string'), 'math_formulas': List(Value('string')), 'char_count': Value('int64')} != {'chunk_id': Value('string'), 'source_file': Value('string'), 'page_number': Value('int64'), 'subject': Value('string'), 'level': Value('string'), 'language': Value('string'), 'specialization': Value('string'), 'chapter': Value('string'), 'section_title': Value('string'), 'content_type': Value('string'), 'content': Value('string'), 'math_formulas': List(Value('null')), 'char_count': Value('int64')}