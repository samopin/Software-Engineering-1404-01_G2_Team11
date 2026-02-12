import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { ThumbsUp, ThumbsDown, GitBranch, Send, ArrowLeft, Loader2 } from 'lucide-react'
import { api } from '../api'

export default function ArticlePage() {
  const { name } = useParams()
  const [article, setArticle] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [voteLoading, setVoteLoading] = useState(false)
  const [publishLoading, setPublishLoading] = useState(false)
  const [message, setMessage] = useState('')

  const fetchArticle = async () => {
    setLoading(true)
    try {
      const data = await api.getArticle(name)
      setArticle(data)
      setError('')
    } catch (err) {
      setError('Failed to load article.')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchArticle()
  }, [name])

  const handleVote = async (value) => {
    setVoteLoading(true)
    setMessage('')
    try {
      const data = await api.vote(name, value)
      setArticle((prev) => ({ ...prev, score: data.score }))
      setMessage(`Vote recorded! Score: ${data.score}`)
    } catch (err) {
      setMessage(err.data?.detail || 'Vote failed.')
    } finally {
      setVoteLoading(false)
    }
  }

  const handlePublish = async () => {
    if (!article?.current_version) return
    setPublishLoading(true)
    setMessage('')
    try {
      const data = await api.publishVersion(article.current_version.name)
      setArticle(data)
      setMessage('Version published successfully!')
    } catch (err) {
      setMessage(err.data?.detail || 'Publish failed.')
    } finally {
      setPublishLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <Loader2 className="w-8 h-8 text-indigo-400 animate-spin" />
      </div>
    )
  }

  if (error) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-16 text-center">
        <p className="text-red-400 text-lg mb-4">{error}</p>
        <Link to="/" className="text-indigo-400 hover:text-indigo-300 underline">
          Back to Home
        </Link>
      </div>
    )
  }

  const version = article?.current_version

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <Link to="/" className="inline-flex items-center gap-2 text-gray-400 hover:text-white mb-6 transition-colors text-sm">
        <ArrowLeft className="w-4 h-4" />
        Back
      </Link>

      <div className="bg-gray-800 rounded-2xl border border-gray-700 overflow-hidden">
        <div className="p-6 border-b border-gray-700">
          <div className="flex items-start justify-between flex-wrap gap-4">
            <div>
              <h1 className="text-2xl font-bold text-white">{article.name}</h1>
              <p className="text-gray-500 text-sm mt-1">
                Creator: <span className="text-gray-400">{article.creator_id}</span>
              </p>
            </div>
            <div className="flex items-center gap-3">
              <div className="flex items-center gap-1 bg-gray-900 rounded-lg px-3 py-2">
                <button
                  onClick={() => handleVote(1)}
                  disabled={voteLoading}
                  className="text-green-400 hover:text-green-300 disabled:opacity-50 transition-colors p-1"
                  title="Upvote"
                >
                  <ThumbsUp className="w-5 h-5" />
                </button>
                <span className="text-white font-bold min-w-[2rem] text-center">
                  {article.score}
                </span>
                <button
                  onClick={() => handleVote(-1)}
                  disabled={voteLoading}
                  className="text-red-400 hover:text-red-300 disabled:opacity-50 transition-colors p-1"
                  title="Downvote"
                >
                  <ThumbsDown className="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
        </div>

        {version ? (
          <div className="p-6">
            <div className="flex items-center justify-between mb-4 flex-wrap gap-3">
              <div className="flex items-center gap-3">
                <span className="text-sm text-gray-400">
                  Version: <span className="text-indigo-400 font-medium">{version.name}</span>
                </span>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={handlePublish}
                  disabled={publishLoading}
                  className="inline-flex items-center gap-1.5 bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors disabled:opacity-50"
                >
                  <Send className="w-4 h-4" />
                  {publishLoading ? 'Publishing...' : 'Publish'}
                </button>
              </div>
            </div>

            {version.summary && (
              <div className="bg-gray-900/50 border border-gray-700 rounded-lg p-4 mb-4">
                <h3 className="text-sm font-semibold text-gray-400 mb-1">Summary</h3>
                <p className="text-gray-300 text-sm">{version.summary}</p>
              </div>
            )}

            {version.tags && version.tags.length > 0 && (
              <div className="flex items-center gap-2 flex-wrap mb-4">
                {version.tags.map((tag) => (
                  <span
                    key={tag.name}
                    className="bg-indigo-500/10 text-indigo-300 text-xs font-medium px-2.5 py-1 rounded-full"
                  >
                    {tag.name}
                  </span>
                ))}
              </div>
            )}

            <div className="bg-gray-900 rounded-lg p-5 mt-4">
              <h3 className="text-sm font-semibold text-gray-400 mb-3">Content</h3>
              <div className="text-gray-300 whitespace-pre-wrap leading-relaxed text-sm" dir="ltr">
                {version.content || 'No content yet.'}
              </div>
            </div>

            <p className="text-xs text-gray-600 mt-3">
              Editor: {version.editor_id}
            </p>
          </div>
        ) : (
          <div className="p-6 text-center text-gray-500">
            No version available for this article.
          </div>
        )}
      </div>

      {message && (
        <div className="mt-4 bg-gray-800 border border-gray-700 rounded-lg p-3 text-sm text-center text-gray-300">
          {message}
        </div>
      )}
    </div>
  )
}
