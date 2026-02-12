const API_BASE = '/api';

async function request(method, path, body = null) {
  const opts = {
    method,
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
  };
  if (body) opts.body = JSON.stringify(body);
  const res = await fetch(`${API_BASE}${path}`, opts);
  const data = await res.json();
  if (!res.ok) throw { status: res.status, data };
  return data;
}

export const api = {
  createArticle: (name) => request('POST', '/articles/create/', { name }),
  getArticle: (name) => request('GET', `/articles/${encodeURIComponent(name)}/`),
  getVersion: (name) => request('GET', `/versions/${encodeURIComponent(name)}/`),
  createVersionFromVersion: (sourceVersionName, newVersionName) =>
    request('POST', '/versions/create/', {
      source_version_name: sourceVersionName,
      new_version_name: newVersionName,
    }),
  publishVersion: (versionName) =>
    request('POST', `/versions/${encodeURIComponent(versionName)}/publish/`),
  vote: (articleName, value) =>
    request('POST', '/vote/', { article_name: articleName, value }),
};
