import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { ThumbsUp, ThumbsDown, GitBranch, Send, ArrowRight, Loader2 } from 'lucide-react'
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
      setError('خطا در بارگذاری مقاله.')
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
      setMessage(`رأی ثبت شد! امتیاز: ${data.score}`)
    } catch (err) {
      setMessage(err.data?.detail || 'خطا در ثبت رأی.')
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
      setMessage('نسخه با موفقیت منتشر شد!')
    } catch (err) {
      setMessage(err.data?.detail || 'خطا در انتشار نسخه.')
    } finally {
      setPublishLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <Loader2 className="w-8 h-8 text-forest animate-spin" />
      </div>
    )
  }

  if (error) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-16 text-center">
        <p className="text-red-600 text-lg mb-4">{error}</p>
        <Link to="/" className="text-forest hover:text-leaf underline">
          بازگشت به خانه
        </Link>
      </div>
    )
  }

  const version = article?.current_version

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <Link to="/" className="inline-flex items-center gap-2 text-gray-500 hover:text-forest mb-6 transition-colors text-sm">
        <ArrowRight className="w-4 h-4" />
        بازگشت
      </Link>

      <div className="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
        <div className="p-6 border-b border-gray-200">
          <div className="flex items-start justify-between flex-wrap gap-4">
            <div>
              <h1 className="text-2xl font-bold text-dark">{article.name}</h1>
              <p className="text-gray-500 text-sm mt-1">
                ایجادکننده: <span className="text-gray-700">{article.creator_id}</span>
              </p>
            </div>
            <div className="flex items-center gap-3">
              <div className="flex items-center gap-1 bg-light rounded-lg px-3 py-2 border border-gray-200">
                <button
                  onClick={() => handleVote(1)}
                  disabled={voteLoading}
                  className="text-forest hover:text-leaf disabled:opacity-50 transition-colors p-1"
                  title="رأی مثبت"
                >
                  <ThumbsUp className="w-5 h-5" />
                </button>
                <span className="text-dark font-bold min-w-[2rem] text-center">
                  {article.score}
                </span>
                <button
                  onClick={() => handleVote(-1)}
                  disabled={voteLoading}
                  className="text-red-500 hover:text-red-400 disabled:opacity-50 transition-colors p-1"
                  title="رأی منفی"
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
                <span className="text-sm text-gray-500">
                  نسخه: <span className="text-forest font-medium">{version.name}</span>
                </span>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={handlePublish}
                  disabled={publishLoading}
                  className="inline-flex items-center gap-1.5 bg-forest hover:bg-leaf text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors disabled:opacity-50"
                >
                  <Send className="w-4 h-4" />
                  {publishLoading ? 'در حال انتشار...' : 'انتشار'}
                </button>
              </div>
            </div>

            {version.summary && (
              <div className="bg-light border border-gray-200 rounded-lg p-4 mb-4">
                <h3 className="text-sm font-semibold text-gray-600 mb-1">خلاصه</h3>
                <p className="text-gray-700 text-sm">{version.summary}</p>
              </div>
            )}

            {version.tags && version.tags.length > 0 && (
              <div className="flex items-center gap-2 flex-wrap mb-4">
                {version.tags.map((tag) => (
                  <span
                    key={tag.name}
                    className="bg-forest/10 text-forest text-xs font-medium px-2.5 py-1 rounded-full"
                  >
                    {tag.name}
                  </span>
                ))}
              </div>
            )}

            <div className="bg-gray-50 rounded-lg p-5 mt-4 border border-gray-200">
              <h3 className="text-sm font-semibold text-gray-600 mb-3">محتوا</h3>
              <div className="text-gray-700 whitespace-pre-wrap leading-relaxed text-sm" dir="ltr">
                {version.content || 'هنوز محتوایی ثبت نشده است.'}
              </div>
            </div>

            <p className="text-xs text-gray-500 mt-3">
              ویرایشگر: {version.editor_id}
            </p>
          </div>
        ) : (
          <div className="p-6 text-center text-gray-500">
            نسخه‌ای برای این مقاله موجود نیست.
          </div>
        )}
      </div>

      {message && (
        <div className="mt-4 bg-white border border-gray-200 rounded-lg p-3 text-sm text-center text-gray-700 shadow-sm">
          {message}
        </div>
      )}
    </div>
  )
}
