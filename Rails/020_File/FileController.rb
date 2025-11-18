class FileController < ApplicationController
  before_action :set_file, only: [:show, :edit, :update, :destroy]

  # GET /file
  def index
    @files = File.all
    render json: @files
  end

  # GET /file/1
  def show
    render json: @file
  end

  # POST /file
  def create
    @file = File.new(file_params)

    if @file.save
      render json: @file, status: :created
    else
      render json: @file.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /file/1
  def update
    if @file.update(file_params)
      render json: @file
    else
      render json: @file.errors, status: :unprocessable_entity
    end
  end

  # DELETE /file/1
  def destroy
    @file.destroy
    head :no_content
  end

  private

  def set_file
    @file = File.find(params[:id])
  end

  def file_params
    params.require(:file).permit(:name)
  end
end
