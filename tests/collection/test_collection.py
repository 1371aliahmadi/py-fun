from src.collection.collection import Collection

def test_contains():
    col = Collection()
    assert col.contains([1, 2, 2, 3], 2) == 2

def test_zip():
    col = Collection()
    assert col.zip([1,2],["a","b"]) == [(1,"a"),(2,"b")]
