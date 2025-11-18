class ThemeController < ApplicationController
  before_action :set_theme, only: [:show, :edit, :update, :destroy]

  # GET /theme
  def index
    @themes = Theme.all
    render json: @themes
  end

  # GET /theme/1
  def show
    render json: @theme
  end

  # POST /theme
  def create
    @theme = Theme.new(theme_params)

    if @theme.save
      render json: @theme, status: :created
    else
      render json: @theme.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /theme/1
  def update
    if @theme.update(theme_params)
      render json: @theme
    else
      render json: @theme.errors, status: :unprocessable_entity
    end
  end

  # DELETE /theme/1
  def destroy
    @theme.destroy
    head :no_content
  end

  private

  def set_theme
    @theme = Theme.find(params[:id])
  end

  def theme_params
    params.require(:theme).permit(:name)
  end
end
