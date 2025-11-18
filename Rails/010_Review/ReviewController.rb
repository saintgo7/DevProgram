class ReviewController < ApplicationController
  before_action :set_review, only: [:show, :edit, :update, :destroy]

  # GET /review
  def index
    @reviews = Review.all
    render json: @reviews
  end

  # GET /review/1
  def show
    render json: @review
  end

  # POST /review
  def create
    @review = Review.new(review_params)

    if @review.save
      render json: @review, status: :created
    else
      render json: @review.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /review/1
  def update
    if @review.update(review_params)
      render json: @review
    else
      render json: @review.errors, status: :unprocessable_entity
    end
  end

  # DELETE /review/1
  def destroy
    @review.destroy
    head :no_content
  end

  private

  def set_review
    @review = Review.find(params[:id])
  end

  def review_params
    params.require(:review).permit(:name)
  end
end
