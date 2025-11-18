class TemplateController < ApplicationController
  before_action :set_template, only: [:show, :edit, :update, :destroy]

  # GET /template
  def index
    @templates = Template.all
    render json: @templates
  end

  # GET /template/1
  def show
    render json: @template
  end

  # POST /template
  def create
    @template = Template.new(template_params)

    if @template.save
      render json: @template, status: :created
    else
      render json: @template.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /template/1
  def update
    if @template.update(template_params)
      render json: @template
    else
      render json: @template.errors, status: :unprocessable_entity
    end
  end

  # DELETE /template/1
  def destroy
    @template.destroy
    head :no_content
  end

  private

  def set_template
    @template = Template.find(params[:id])
  end

  def template_params
    params.require(:template).permit(:name)
  end
end
