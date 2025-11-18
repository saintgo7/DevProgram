class CommentController < ApplicationController
  before_action :set_comment, only: [:show, :edit, :update, :destroy]

  # GET /comment
  def index
    @comments = Comment.all
    render json: @comments
  end

  # GET /comment/1
  def show
    render json: @comment
  end

  # POST /comment
  def create
    @comment = Comment.new(comment_params)

    if @comment.save
      render json: @comment, status: :created
    else
      render json: @comment.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /comment/1
  def update
    if @comment.update(comment_params)
      render json: @comment
    else
      render json: @comment.errors, status: :unprocessable_entity
    end
  end

  # DELETE /comment/1
  def destroy
    @comment.destroy
    head :no_content
  end

  private

  def set_comment
    @comment = Comment.find(params[:id])
  end

  def comment_params
    params.require(:comment).permit(:name)
  end
end
