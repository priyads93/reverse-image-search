CREATE EXTENSION vector;

CREATE TABLE image_search_l14 (
  id UUID PRIMARY KEY,
  url TEXT,
  embedding vector(768)
);

CREATE INDEX ON image_search_l14 USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);