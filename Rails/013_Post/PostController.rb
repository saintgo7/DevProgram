class PostController < ApplicationController
  before_action :set_post, only: [:show, :edit, :update, :destroy]

  # GET /post
  def index
    @posts = Post.all
    render json: @posts
  end

  # GET /post/1
  def show
    render json: @post
  end

  # POST /post
  def create
    @post = Post.new(post_params)

    if @post.save
      render json: @post, status: :created
    else
      render json: @post.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /post/1
  def update
    if @post.update(post_params)
      render json: @post
    else
      render json: @post.errors, status: :unprocessable_entity
    end
  end

  # DELETE /post/1
  def destroy
    @post.destroy
    head :no_content
  end

  private

  def set_post
    @post = Post.find(params[:id])
  end

  def post_params
    params.require(:post).permit(:name)
  end
end
