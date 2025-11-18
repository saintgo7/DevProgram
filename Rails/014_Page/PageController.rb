class PageController < ApplicationController
  before_action :set_page, only: [:show, :edit, :update, :destroy]

  # GET /page
  def index
    @pages = Page.all
    render json: @pages
  end

  # GET /page/1
  def show
    render json: @page
  end

  # POST /page
  def create
    @page = Page.new(page_params)

    if @page.save
      render json: @page, status: :created
    else
      render json: @page.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /page/1
  def update
    if @page.update(page_params)
      render json: @page
    else
      render json: @page.errors, status: :unprocessable_entity
    end
  end

  # DELETE /page/1
  def destroy
    @page.destroy
    head :no_content
  end

  private

  def set_page
    @page = Page.find(params[:id])
  end

  def page_params
    params.require(:page).permit(:name)
  end
end
