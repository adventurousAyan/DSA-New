curl --header "Content-Type: application/json" --request POST   --data '[
  {
    "model_name": "test_model.pkl",
    "model_version": "v1",
    "model_type": "pkl",
    "model_path": "models",
    "client_id": "1234",
    "product_name": "testproduct",
    "model_path_type": "NFS"
  }
]' http://127.0.0.1:5000/api/deploy