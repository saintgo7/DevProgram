class SanitizerController < ApplicationController
  before_action :set_sanitizer, only: [:show, :edit, :update, :destroy]

  # GET /sanitizer
  def index
    @sanitizers = Sanitizer.all
    render json: @sanitizers
  end

  # GET /sanitizer/1
  def show
    render json: @sanitizer
  end

  # POST /sanitizer
  def create
    @sanitizer = Sanitizer.new(sanitizer_params)

    if @sanitizer.save
      render json: @sanitizer, status: :created
    else
      render json: @sanitizer.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /sanitizer/1
  def update
    if @sanitizer.update(sanitizer_params)
      render json: @sanitizer
    else
      render json: @sanitizer.errors, status: :unprocessable_entity
    end
  end

  # DELETE /sanitizer/1
  def destroy
    @sanitizer.destroy
    head :no_content
  end

  private

  def set_sanitizer
    @sanitizer = Sanitizer.find(params[:id])
  end

  def sanitizer_params
    params.require(:sanitizer).permit(:name)
  end
end
