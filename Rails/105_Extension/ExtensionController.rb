class ExtensionController < ApplicationController
  before_action :set_extension, only: [:show, :edit, :update, :destroy]

  # GET /extension
  def index
    @extensions = Extension.all
    render json: @extensions
  end

  # GET /extension/1
  def show
    render json: @extension
  end

  # POST /extension
  def create
    @extension = Extension.new(extension_params)

    if @extension.save
      render json: @extension, status: :created
    else
      render json: @extension.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /extension/1
  def update
    if @extension.update(extension_params)
      render json: @extension
    else
      render json: @extension.errors, status: :unprocessable_entity
    end
  end

  # DELETE /extension/1
  def destroy
    @extension.destroy
    head :no_content
  end

  private

  def set_extension
    @extension = Extension.find(params[:id])
  end

  def extension_params
    params.require(:extension).permit(:name)
  end
end
