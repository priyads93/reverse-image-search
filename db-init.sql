CREATE EXTENSION vector;

CREATE TABLE image_search (
  id UUID PRIMARY KEY,
  url TEXT,
  embedding vector(512)
);

CREATE INDEX ON image_search USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);