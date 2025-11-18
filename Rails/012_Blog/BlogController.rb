class BlogController < ApplicationController
  before_action :set_blog, only: [:show, :edit, :update, :destroy]

  # GET /blog
  def index
    @blogs = Blog.all
    render json: @blogs
  end

  # GET /blog/1
  def show
    render json: @blog
  end

  # POST /blog
  def create
    @blog = Blog.new(blog_params)

    if @blog.save
      render json: @blog, status: :created
    else
      render json: @blog.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /blog/1
  def update
    if @blog.update(blog_params)
      render json: @blog
    else
      render json: @blog.errors, status: :unprocessable_entity
    end
  end

  # DELETE /blog/1
  def destroy
    @blog.destroy
    head :no_content
  end

  private

  def set_blog
    @blog = Blog.find(params[:id])
  end

  def blog_params
    params.require(:blog).permit(:name)
  end
end
