class ArchiveController < ApplicationController
  before_action :set_archive, only: [:show, :edit, :update, :destroy]

  # GET /archive
  def index
    @archives = Archive.all
    render json: @archives
  end

  # GET /archive/1
  def show
    render json: @archive
  end

  # POST /archive
  def create
    @archive = Archive.new(archive_params)

    if @archive.save
      render json: @archive, status: :created
    else
      render json: @archive.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /archive/1
  def update
    if @archive.update(archive_params)
      render json: @archive
    else
      render json: @archive.errors, status: :unprocessable_entity
    end
  end

  # DELETE /archive/1
  def destroy
    @archive.destroy
    head :no_content
  end

  private

  def set_archive
    @archive = Archive.find(params[:id])
  end

  def archive_params
    params.require(:archive).permit(:name)
  end
end
